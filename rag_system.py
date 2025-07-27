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
import uuid
import pdfplumber
import pytesseract
from PIL import Image

# Load environment variables
load_dotenv("config.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGSystem:
    """Full RAG system for PDF loading, chunking, embedding, and psql vector storage."""
    
    def __init__(self):
        # set variables from environment
        self.embedding_model_name = os.getenv("EMBEDDING_MODEL", "BAAI/bge-large-en-v1.5")
        self.knowledge_base_dir = os.getenv("KNOWLEDGE_BASE_DIR", "./knowledge_base")
        
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
        elements = partition_pdf(file_path, strategy="hi_res", ocr_languages=["eng"])
        logger.info(f"Extracted {len(elements)} elements from PDF")
        return elements

    def group_semantic_chunks(self, elements, file_path):
        chunks = []
        current_section = {
            "title": "Untitled Section",
            "subsections": [],
            "content": [],
            "page_numbers": set()
        }

        current_subsection = None

        def save_current_section():
            if current_section["content"] or current_section["subsections"]:
                chunks.append({
                    "chunk_id": str(uuid.uuid4()),
                    "title": current_section["title"],
                    "content": "\n".join(current_section["content"]).strip(),
                    "subsections": current_section["subsections"],
                    "source": os.path.basename(file_path),
                    "page_numbers": sorted(list(current_section["page_numbers"])),
                })

        def save_current_subsection():
            if current_subsection and current_subsection["content"]:
                current_section["subsections"].append({
                    "title": current_subsection["title"],
                    "content": "\n".join(current_subsection["content"]).strip(),
                    "page_numbers": sorted(list(current_subsection["page_numbers"])),
                })

        for el in elements:
            category = el.category or "Unknown"
            text = (el.text or "").strip()

            # Skip completely if it's not useful
            if category in ["Header", "Footer", "Image", "PageBreak", "UncategorizedText"]:
                continue
            if not text:
                continue

            # Clean up the text and page info
            page = el.metadata.page_number or 1

            # Skip "Contents" section — common in PDFs with no use for rag 
            if category == "Title" and text.lower().strip() in ["contents", "table of contents"]:
                continue

            # Start new section if we find a Title
            if category == "Title":
                save_current_subsection()
                save_current_section()
                current_section = {
                    "title": text,
                    "subsections": [],
                    "content": [],
                    "page_numbers": {page}
                }
                current_subsection = None
                continue

            # Detect and handle subsections (e.g., by pattern or category)
            if category in ["SectionHeader", "Heading"]:
                save_current_subsection()
                current_subsection = {
                    "title": text,
                    "content": [],
                    "page_numbers": {page}
                }
                continue

            # Otherwise, add as regular content
            if current_subsection:
                current_subsection["content"].append(text)
                current_subsection["page_numbers"].add(page)
            else:
                current_section["content"].append(text)
                current_section["page_numbers"].add(page)

        # Save  last chunk
        save_current_subsection()
        save_current_section()

        return chunks
    def summarize_table(self, rows, max_rows=15): 
        if not rows:
            return "No rows found."

        headers = list(rows[0].keys())
        lines = [" | ".join(headers), " | ".join(["---"] * len(headers))]

        
        effective_max = max_rows if len(rows) > max_rows else len(rows)
        
        for i, row in enumerate(rows):
            if i >= effective_max:
                remaining = len(rows) - effective_max
                lines.append(f"...and {remaining} more rows.")
                break
            line = " | ".join(row.get(h, "") for h in headers)
            lines.append(line)

        return "\n".join(lines)
    def extract_tables_and_images(self, elements, file_path):
        """Simple table and image extraction using only tesseract OCR."""
        chunks = []
        doc_name = os.path.basename(file_path)

        # Get page titles for context
        page_titles = {}
        for el in elements:
            if el.category == "Title" and el.metadata and el.metadata.page_number:
                pg = el.metadata.page_number
                page_titles.setdefault(pg, []).append(el.text.strip())

        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_num = i + 1

                # Extract tables using pdfplumber only
                try:
                    tables = page.extract_tables()
                    if tables:
                        logger.info(f"[PDF Page {page_num}] Found {len(tables)} tables")

                    for table in tables:
                        if not table or len(table) <= 1:
                            continue
                            
                        headers = table[0] if table[0] else []
                        rows = table[1:]

                        # Create structured data with null handling
                        structured_data = []
                        for row in rows:
                            if row:  # Skip empty rows
                                record = {}
                                for col_idx, cell in enumerate(row):
                                    header = headers[col_idx] if col_idx < len(headers) and headers[col_idx] else f"Column_{col_idx+1}"
                                    record[header] = str(cell).strip() if cell else "-"
                                structured_data.append(record)

                        if structured_data:  # Only add if we have valid data
                            title_texts = page_titles.get(page_num, [])
                            title = title_texts[-1] if title_texts else f"Table (Page {page_num})"

                            chunks.append({
                                "chunk_id": str(uuid.uuid4()),
                                "title": title,
                                "type": "table",
                                "content": self.summarize_table(structured_data),
                                "raw_table": structured_data,
                                "page_numbers": [page_num],
                                "source": doc_name
                            })
                except Exception as e:
                    logger.warning(f"Table extraction failed on page {page_num}: {e}")

                # Simple image OCR with tesseract 
                try:
                    for img_dict in page.images:
                        x0, top, x1, bottom = img_dict["x0"], img_dict["top"], img_dict["x1"], img_dict["bottom"]
                        
                        # Skip small images (logos, decorative elements)
                        width, height = x1 - x0, bottom - top
                        if width < 100 or height < 100:
                            continue
                            
                        cropped_image = page.to_image(resolution=150).original.crop((x0, top, x1, bottom)).convert("RGB")
                        ocr_text = pytesseract.image_to_string(cropped_image).strip()
                        
                        # Only add if OCR found meaningful text
                        if len(ocr_text) > 15:
                            chunks.append({
                                "chunk_id": str(uuid.uuid4()),
                                "title": f"Image Text (Page {page_num})",
                                "type": "image",
                                "content": ocr_text,
                                "page_numbers": [page_num],
                                "source": doc_name
                            })

                except Exception as e:
                    logger.warning(f"Image OCR failed on page {page_num}: {e}")

        return chunks
    def parse_pdf_combined(self, file_path):
        """Parse PDF using combined semantic and visual extraction."""
        # Step 1: Semantic elements
        elements = self.load_pdf_elements(file_path)
        semantic_chunks = self.group_semantic_chunks(elements, file_path)

        # Step 2: Visual elements (tables/images)
        visual_chunks = self.extract_tables_and_images(elements, file_path)

        # Step 3: Combine and return
        return semantic_chunks + visual_chunks

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
                # Use the new combined parsing function
                all_chunks = self.parse_pdf_combined(full_path)
                
                chunked_data = []
                for i, chunk in enumerate(all_chunks):
                    # Handle different chunk types
                    if chunk.get('type') in ['table', 'image', 'image-table']:
                        # For visual chunks, use caption or content
                        if chunk.get('type') == 'table':
                            text = f"{chunk['title']}\n{chunk['content']}"
                        else:
                            text = f"{chunk['title']}\n{chunk.get('caption', '')}"
                    else:
                        # For semantic chunks, combine title and content
                        text = f"{chunk['title']}\n{chunk['content']}"
                    
                    # Get page number from the new structure
                    page_numbers = chunk.get('page_numbers', [])
                    page_number = min(page_numbers) if page_numbers else None
                    
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
                logger.info(f"Successfully processed {full_path} with {len(all_chunks)} chunks")
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
    
    # Build index (automatically overwrites existing embeddings per file)
    rag.build_index()
    
    # Test search
    test_query = "What is the dress code policy?"
    context, similarity = rag.get_rag_context(test_query)
    
    print(f"Query: {test_query}")
    print(f"Max Similarity: {similarity:.3f}")
    print(f"Context: {context[:200]}..." if context else "No context above threshold")
