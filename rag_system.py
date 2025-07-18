import os
import logging
from pathlib import Path
from typing import List, Optional, Tuple
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import psycopg2
from psycopg2.extras import execute_values
import re
from unstructured.partition.pdf import partition_pdf

# Load environment variables
load_dotenv("config.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGSystem:
    """Full RAG system for PDF loading, chunking, embedding, and psql vector storage."""
    
    def __init__(self):
        # set variables from environment
        self.embedding_model_name = os.getenv("EMBEDDING_MODEL", "BAAI/bge-large-en-v1.5")
        self.knowledge_base_dir = os.getenv("KNOWLEDGE_BASE_DIR", "../knowledge_base")
        
        # database configuration
        self.db_config = {
            'host': os.getenv('PGHOST', 'localhost'),
            'port': int(os.getenv('PGPORT', '5433')),
            'database': 'test',
            'user': os.getenv('PGUSER', 'postgres'),
            'password': os.getenv('PGPASSWORD', 'password')
        }
        
        # initialize components
        
        # Load embedding model
        logger.info(f"Loading embedding model: {self.embedding_model_name}")
        self.embedding_model = SentenceTransformer(self.embedding_model_name)
        self.embedding_dim = self.embedding_model.get_sentence_embedding_dimension()
        
        # Initialize database
        self._init_database()
        self.ensure_index_exists()
    
    def _get_connection(self):
        """Get database connection."""
        return psycopg2.connect(**self.db_config)
    
    def _init_database(self):
        """Initialize database tables for embeddings and chat history."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    # Enable pgvector extension
                    eng.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                    
                    # Check if table exists
                    eng.execute("""
                        SELECT COUNT(*) 
                        FROM information_schema.tables 
                        WHERE table_name = 'document_embeddings'
                    """)
                    table_exists = eng.fetchone()[0] > 0
                    
                    if table_exists:
                        # Check if table has data
                        eng.execute("SELECT COUNT(*) FROM document_embeddings")
                        
                        
                    # create embeddings table
                    eng.execute(f"""
                        CREATE TABLE IF NOT EXISTS document_embeddings (
                            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                            content TEXT NOT NULL,
                            embedding vector({self.embedding_dim}) NOT NULL,
                            source_file VARCHAR(255),
                            page_number INTEGER,
                            chunk_index INTEGER,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    
                    # Create index for vector similarity search
                    eng.execute("""
                        CREATE INDEX IF NOT EXISTS document_embeddings_vector_idx 
                        ON document_embeddings USING ivfflat (embedding vector_cosine_ops)
                        WITH (lists = 100);
                    """)
                    
                    # Create chat sessions table
                    eng.execute("""
                        CREATE TABLE IF NOT EXISTS chat_sessions (
                            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                            title VARCHAR(255)
                        );
                    """)
                    # Drop timestamp columns if they exist
                    eng.execute("ALTER TABLE chat_sessions DROP COLUMN IF EXISTS created_at;")
                    eng.execute("ALTER TABLE chat_sessions DROP COLUMN IF EXISTS updated_at;")
                    # Create chat messages table
                    eng.execute("""
                        CREATE TABLE IF NOT EXISTS chat_messages (
                            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                            session_id UUID REFERENCES chat_sessions(id) ON DELETE CASCADE,
                            role VARCHAR(255) NOT NULL CHECK (role IN ('user', 'assistant')),
                            content TEXT NOT NULL,
                            rag_context TEXT,
                            similarity_score FLOAT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    
                    conn.commit()
            logger.info(" Database tables initialized successfully")
            
            # Validate the setup
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute("SELECT COUNT(*) FROM document_embeddings")
                    count = eng.fetchone()[0]
                    logger.info(f" Vector database ready - {count} embeddings stored")
                    
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            raise
    
    def load_pdf_elements(self, file_path: str) -> List:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        logger.info(f"Loading PDF with unstructured: {file_path}")
        elements = partition_pdf(file_path, strategy="hi_res")
        logger.info(f"Extracted {len(elements)} elements from PDF")
        return elements

    def group_semantic_chunks(self, elements, file_path):
        chunks = []
        current_title = "Untitled Section"
        current_content = []
        current_pages = set()
        for el in elements:
            if el.category in ["Header", "Footer"]:
                continue
            text = el.text.strip()
            if not text:
                continue
            # Preprocess: remove >5 newlines and >10 dots in a row
            text = re.sub(r'\n{6,}', '\n', text)
            text = re.sub(r'\.{11,}', '', text)
            if hasattr(el.metadata, 'page_number') and el.metadata.page_number:
                current_pages.add(el.metadata.page_number)
            if el.category == "Title":
                if current_content:
                    chunks.append({
                        "title": current_title,
                        "content": "\n".join(current_content),
                        "source": os.path.basename(file_path),
                        "pages": list(current_pages)
                    })
                    current_content = []
                    current_pages = set()
                current_title = text
            else:
                current_content.append(text)
        if current_content:
            chunks.append({
                "title": current_title,
                "content": "\n".join(current_content),
                "source": os.path.basename(file_path),
                "pages": list(current_pages)
            })
        return chunks

    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for a list of texts."""
        embeddings = self.embedding_model.encode(texts, normalize_embeddings=True)
        return embeddings
    
    def store_embeddings(self, chunked_data: List[Tuple[str, dict]], embeddings: np.ndarray):
        """Store text chunks and their embeddings in the database."""
        logger.info(f"Storing {len(chunked_data)} embeddings in database")
        
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    # Clear existing embeddings for this source file
                    source_file = chunked_data[0][1]['source_file'] if chunked_data else 'unknown'
                    eng.execute("DELETE FROM document_embeddings WHERE source_file = %s", (source_file,))
                    
                    # Prepare data for batch insert
                    insert_data = []
                    for (text, metadata), embedding in zip(chunked_data, embeddings):
                        insert_data.append((
                            text,
                            embedding.tolist(),
                            metadata['source_file'],
                            metadata['page_number'],
                            metadata['chunk_index']
                        ))
                    
                    # Batch insert
                    execute_values(
                        eng,
                        """INSERT INTO document_embeddings 
                           (content, embedding, source_file, page_number, chunk_index) 
                           VALUES %s""",
                        insert_data,
                        template=None,
                        page_size=100
                    )
                    
                    conn.commit()
            logger.info("Embeddings stored successfully")
        except Exception as e:
            logger.error(f"Error storing embeddings: {e}")
            raise
    
    def build_index(self, dir_path: Optional[str] = None):
        """Complete pipeline: load PDFs from directory, chunk, embed, and store."""
        logger.info("Building RAG index...")
        
        dir_path = dir_path or self.knowledge_base_dir
        if not os.path.exists(dir_path):
            logger.error(f"Knowledge base directory not found: {dir_path}")
            return
        
        pdf_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {dir_path}")
            return
        
        for pdf_file in pdf_files:
            full_path = os.path.join(dir_path, pdf_file)
            try:
                elements = self.load_pdf_elements(full_path)
                semantic_chunks = self.group_semantic_chunks(elements, full_path)
                
                chunked_data = []
                for i, chunk in enumerate(semantic_chunks):
                    text = f"{chunk['title']}\n{chunk['content']}"
                    page_number = min(chunk['pages']) if chunk['pages'] else None
                    metadata = {
                        'chunk_index': i,
                        'page_number': page_number,
                        'source_file': chunk['source']
                    }
                    chunked_data.append((text, metadata))
                
                if not chunked_data:
                    logger.warning(f"No chunks created from {full_path}")
                    continue
                
                texts = [chunk[0] for chunk in chunked_data]
                embeddings = self.generate_embeddings(texts)
                
                self.store_embeddings(chunked_data, embeddings)
                logger.info(f"Successfully processed {full_path}")
            except Exception as e:
                logger.error(f"Error processing {full_path}: {str(e)}")
        
        logger.info("RAG index built successfully")
    
    def ensure_index_exists(self):
        """Ensure the RAG index exists, rebuild if necessary."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute("SELECT COUNT(*) FROM document_embeddings")
                    count = eng.fetchone()[0]
                    
                    if count == 0:
                        logger.info("No embeddings found, rebuilding index...")
                        self.build_index()
                        return True
                    else:
                        logger.info(f"Index exists with {count} embeddings")
                        return False
        except Exception as e:
            logger.error(f"Error checking index: {e}")
            return False

    def search_similar(self, query: str, k: int = None) -> List[Tuple[str, float]]:
        """Search for similar text chunks using vector similarity."""
        k = k or int(os.getenv("RETRIEVAL_K", "4"))
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query], normalize_embeddings=True)[0]
        
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    # First check if we have any embeddings
                    eng.execute("SELECT COUNT(*) FROM document_embeddings")
                    count = eng.fetchone()[0]
                    logger.info(f"Database contains {count} embeddings for search")
                    
                    if count == 0:
                        logger.warning("No embeddings found in database!")
                        return []
                    
                    # Perform similarity search
                    eng.execute("""
                        SELECT content, (1 - (embedding <=> %s::vector)) as similarity
                        FROM document_embeddings
                        ORDER BY embedding <=> %s::vector
                        LIMIT %s
                    """, (query_embedding.tolist(), query_embedding.tolist(), k))
                    
                    results = eng.fetchall()
                    logger.info(f"Found {len(results)} similar chunks for query: '{query[:50]}...'")
                    if results:
                        logger.info(f"Top similarity score: {results[0][1]:.3f}")
                    return [(content, float(similarity)) for content, similarity in results]
        except Exception as e:
            logger.error(f"Error searching similar texts: {e}")
            return []
    
    def get_rag_context(self, query: str, similarity_threshold: float = None) -> Tuple[str, float]:
        """Get RAG context for a query if similarity score is above threshold."""
        similarity_threshold = similarity_threshold or float(os.getenv("SIMILARITY_THRESHOLD", "0.7"))
        
        similar_chunks = self.search_similar(query)
        
        if not similar_chunks:
            return "", 0.0
        
        # Get the highest similarity score
        max_similarity = similar_chunks[0][1] if similar_chunks else 0.0
        
        # Return context only if above threshold
        if max_similarity >= similarity_threshold:
            context_parts = []
            for content, similarity in similar_chunks:
                context_parts.append(f"[Similarity: {similarity:.3f}]\n{content}")
            
            context = "\n\n---\n\n".join(context_parts)
            return context, max_similarity
        
        return "", max_similarity


if __name__ == "__main__":
    # Test the RAG system
    rag = RAGSystem()
    
    # Build index
    rag.build_index()
    
    # Test search
    test_query = "What is the dress code policy?"
    context, similarity = rag.get_rag_context(test_query)
    
    print(f"Query: {test_query}")
    print(f"Max Similarity: {similarity:.3f}")
    print(f"Context: {context[:200]}..." if context else "No context above threshold")
