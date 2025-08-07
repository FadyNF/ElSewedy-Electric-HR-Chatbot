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
import uuid
from llama_parse import LlamaParse

# Load environment variables
load_dotenv("config.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGSystem:
    """Clean RAG system using LlamaParse for PDF processing and PostgreSQL for vector storage."""
    
    def __init__(self):
        # Set variables from environment
        self.embedding_model_name = os.getenv("EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-0.6B")
        self.knowledge_base_dir = os.getenv("KNOWLEDGE_BASE_DIR", "d:/ELSEWEDY/ElSewedy-Electric-HR-Chatbot/knowledge_base")
        
        # LlamaParse configuration
        self.llama_cloud_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

        # Database configuration
        self.db_config = {
            'host': os.getenv('PGHOST', 'localhost'),
            'port': int(os.getenv('PGPORT', '5433')),
            'database': 'test',
            'user': os.getenv('PGUSER', 'postgres'),
            'password': os.getenv('PGPASSWORD', 'password')
        }
        
        # Initialize components
        logger.info(f"Loading embedding model: {self.embedding_model_name}")
        self.embedding_model = SentenceTransformer(self.embedding_model_name)
        self.embedding_dim = self.embedding_model.get_sentence_embedding_dimension()
        
        # Initialize LlamaParse
        self.parser = LlamaParse(
            api_key=self.llama_cloud_api_key,
            result_type="markdown",  # Get structured markdown output
            verbose=True,
            language="en",
            table_extraction=True,  
            split_by_page=False,  
            premium_quality_parsing=True  
        )
        
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
    
    def parse_pdf_with_llamaparse(self, file_path: str) -> str:
        """Parse PDF using LlamaParse to get structured markdown content."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        logger.info(f"Parsing PDF with LlamaParse: {file_path}")
        
        try:
            # Parse the document
            documents = self.parser.load_data(file_path)
            
            if not documents:
                logger.warning(f"No content extracted from {file_path}")
                return ""
            
            # Combine all document content
            full_content = "\n\n".join([doc.text for doc in documents])
            logger.info(f"Successfully parsed {file_path} - {len(full_content)} characters extracted")
            
            return full_content
            
        except Exception as e:
            logger.error(f"Error parsing PDF with LlamaParse: {e}")
            return ""
    def clean_and_filter_text(self, text: str) -> str:
        """Apply basic text preprocessing and remove unwanted content."""
        if not text or len(text.strip()) < 10:
            return ""
        text = text.strip()
        # Remove website links
        if 'www.elsewedyelectric.com' in text.lower():
            logger.info(f"Found website link in text: {text[:100]}...")
        text = re.sub(r'www\.elsewedyelectric\.com', '', text, flags=re.IGNORECASE)
        if 'www.elsewedyelectric.com' in text.lower():
            logger.warning(f"Website link still present after removal attempt!")
        else:
            logger.debug(f"Website link successfully removed or not present")
        # Remove lines with 5+ consecutive dots (contents pages)
        text = re.sub(r'^.*\.{5,}.*$', '', text, flags=re.MULTILINE)
        # Remove excessive newlines (more than 3 consecutive- title pages)
        text = re.sub(r'\n{4,}', '\n\n', text)
        # Clean up any remaining whitespace
        text = text.strip() 
        # Skip page numbers and formatting
        if re.match(r'^[\d\s\.\-_]+$', text.strip()):
            return ""
        return text.strip()
    #Chunking : Cause of most issues in system.
    def chunk_markdown_content(self, content: str, file_path: str) -> List[dict]:
        """Chunk the markdown content into semantic sections."""
        chunks = []
        doc_name = os.path.basename(file_path)
        
        # Split content by headers (markdown style)
        sections = re.split(r'\n(?=#+\s)', content)
        
        for i, section in enumerate(sections):
            if not section.strip():
                continue
            
            # Clean the section content
            cleaned_content = self.clean_and_filter_text(section)
            if not cleaned_content:
                continue
            
            # Extract title from first line if it's a header
            lines = cleaned_content.split('\n')
            if lines[0].startswith('#'):
                title = re.sub(r'^#+\s*', '', lines[0]).strip()
                content_body = '\n'.join(lines[1:]).strip()
            else:
                title = f"Section {i+1}"
                content_body = cleaned_content
            
            if content_body and len(content_body.strip()) > 10:  # Only add if there's content
                chunks.append({
                    "chunk_id": str(uuid.uuid4()),
                    "title": title,
                    "content": content_body,
                    "source": doc_name,
                    "chunk_index": i
                })
        
        logger.info(f"Created {len(chunks)} chunks from {doc_name}")
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
        """Complete pipeline: load PDFs from directory, parse with LlamaParse, chunk, embed, and store."""
        logger.info("Building RAG index with LlamaParse...")
        
        dir_path = dir_path or self.knowledge_base_dir
        pdf_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.pdf')]
        # Loop over files
        for pdf_file in pdf_files:
            full_path = os.path.join(dir_path, pdf_file)
            try:
                # parse PDF
                content = self.parse_pdf_with_llamaparse(full_path)
                if not content:
                    logger.warning(f"No content extracted from {full_path}")
                    continue
                
                # Chunk the content
                chunks = self.chunk_markdown_content(content, full_path)
                
                if not chunks:
                    logger.warning(f"No chunks created from {full_path}")
                    continue
                
                # Prepare data for embedding
                chunked_data = []
                for chunk in chunks:
                    text = f"{chunk['title']}\n{chunk['content']}"
                    metadata = {
                        'chunk_index': chunk['chunk_index'],
                        'page_number': None,
                        'source_file': chunk['source']
                    }
                    chunked_data.append((text, metadata))
                
                # Generate embeddings and store
                texts = [chunk[0] for chunk in chunked_data]
                embeddings = self.generate_embeddings(texts)
                
                self.store_embeddings(chunked_data, embeddings)
                logger.info(f"Successfully processed {full_path} with {len(chunks)} chunks")
                
            except Exception as e:
                logger.error(f"Error processing {full_path}: {str(e)}")
        
        logger.info("RAG index built successfully with LlamaParse")
    
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
        similarity_threshold = similarity_threshold or float(os.getenv("SIMILARITY_THRESHOLD", "0.6"))
        
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
    
    # Build index (automatically overwrites existing embeddings per file)
    rag.build_index()