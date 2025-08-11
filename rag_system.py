import os
import logging
from pathlib import Path
from typing import List, Optional
import re
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_unstructured import UnstructuredLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
# Load environment variables
load_dotenv("config.env")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class RAGSystem:
    """LangChain-powered RAG system with structured document loading and vector storage."""    
    def __init__(self):
        # Paths and config
        self.embedding_model_name = os.getenv("EMBEDDING_MODEL")
        self.knowledge_base_dir = os.getenv("KNOWLEDGE_BASE_DIR")
        
        # LangChain embeddings
        logger.info(f"Loading embedding model: {self.embedding_model_name}")
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model_name)
        
        # Chroma vector store
        chroma_store_path = os.getenv("CHROMA_STORE_PATH")
        logger.info(f"Initializing Chroma at: {chroma_store_path}")
        
        # load existing vector store
        if os.path.exists(chroma_store_path) and os.listdir(chroma_store_path):
            self.vectorstore = Chroma(
                persist_directory=chroma_store_path,
                embedding_function=self.embeddings,
                collection_name="knowledge_base"
            )
        else:
            self.vectorstore = None
            
        # Text splitter for final chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )

    def clean_and_filter_text(self, text: str) -> str:
        """Clean OCR artifacts and filter junk text."""
        if not text or len(text.strip()) < 30:
            return ""
        
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Length and word count filters
        if len(text) < 200 or len(text.split()) < 20:
            return ""
        
        # Skip chunks that are mostly fragmented words
        words = text.split()
        short_words = sum(1 for word in words if len(word) < 3)
        if short_words / len(words) > 0.5:  # More than 50% very short words
            return ""
        
        # Quick filters - return early if junk detected
        junk_patterns = [
            r'[A-Z]\s+[A-Z]\s+[A-Z]',                          # Spaced letters
            r'[\u0600-\u06FF][A-Z]{1,3}[\u0600-\u06FF]',       # Mixed Arabic/Latin
            r'[£\\~_]{2,}|[^\w\s\u0600-\u06FF]{4,}',           # Symbols/weird chars
            r'(.)\1{5,}',                                       # Repeated chars
            r'^(~~+|\.+|-+|_+|\d+\.?|Contents)$',              # Standalone junk
            r'.*\.{3,}.*\d+$'                                   # Table of contents
        ]
        
        for pattern in junk_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return ""
        
        # Filter by special character ratio
        if len(re.findall(r'[^\w\s\u0600-\u06FF]', text)) / len(text) > 0.3:
            return ""
        
        # Clean and return
        return re.sub(r'www\.elsewedy.*?\.com|\.{3,}|\d+\.?$', '', text, flags=re.IGNORECASE).strip()

    def process_document(self, file_path: str) -> List[str]:
        """Process a single document using UnstructuredFileLoader"""
        logger.info(f"Processing document: {os.path.basename(file_path)}")
        
        try:
            # Load with structured elements
            loader = UnstructuredLoader(
                file_path,
                mode="elements",      # structured elements, in reading order
                strategy="hi_res", 
                hi_res_model_name="yolox",
                pdf_infer_table_structure=True,
                extract_images_in_pdf=True,
                languages=["ara", "eng"], 
            )
            
            elements = loader.load()
            logger.info(f"Loaded {len(elements)} elements from {os.path.basename(file_path)}")
            
            # Separate tables from regular text
            table_elements = [el for el in elements if el.metadata.get('category') == 'Table']
            text_elements = [el for el in elements if el.metadata.get('category') != 'Table']
            
            # Clean text 
            cleaned_texts = []
            for element in text_elements:
                cleaned_content = self.clean_and_filter_text(element.page_content)
                if cleaned_content:  # Only keep non-empty results
                    cleaned_texts.append(cleaned_content)
                    
            # Process tables separately to preserve structure
            table_chunks = []
            for table_el in table_elements:
                table_text = table_el.page_content.strip()
                if len(table_text) > 100 and table_text.count('.') < len(table_text) * 0.4:
                    table_chunks.append(f"[TABLE] {table_text}")
            
            logger.info(f"After cleaning: {len(cleaned_texts)} valid text elements")
            
            # Merge small elements before chunking to avoid tiny chunks
            merged_text = "\n\n".join(cleaned_texts)
            logger.info(f"Merged text length: {len(merged_text)} characters")
            # Apply text splitter for final chunking
            split_chunks = self.text_splitter.split_text(merged_text)
            
            # Filter chunks again after splitting (splitting might create junk chunks)
            final_chunks = []
            for chunk in split_chunks:
                cleaned_chunk = self.clean_and_filter_text(chunk)
                if cleaned_chunk:
                    final_chunks.append(cleaned_chunk)
            
            # Add table chunks
            final_chunks.extend(table_chunks)

            logger.info(f"Created {len(final_chunks)} final chunks from {os.path.basename(file_path)}")
            
            # Debug: show first few chunks with better info
            for i, chunk in enumerate(final_chunks[:2]):
                logger.info(f"Sample chunk {i+1} ({len(chunk)} chars): {chunk[:100]}...")
            
            return final_chunks
            
        except Exception as e:
            logger.error(f"Error processing document {file_path}: {str(e)}")
            return []
    
    def build_index(self, dir_path: Optional[str] = None):
        """Build the vector index from all PDFs in the directory."""
        logger.info("Building RAG index with LangChain + UnstructuredFileLoader...")
        
        dir_path = dir_path or self.knowledge_base_dir
        pdf_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {dir_path}")
            return
        
        all_chunks = []
        all_metadatas = []
        
        for pdf_file in pdf_files:
            full_path = os.path.join(dir_path, pdf_file)
            chunks = self.process_document(full_path)
            
            if chunks:
                all_chunks.extend(chunks)
                # Add metadata for each chunk
                metadatas = [{"source_file": pdf_file, "chunk_index": i} for i in range(len(chunks))]
                all_metadatas.extend(metadatas)
        
        if not all_chunks:
            logger.warning("No content extracted from any documents")
            return
        
        # Create vector store from all chunks
        chroma_store_path = os.getenv("CHROMA_STORE_PATH")
        self.vectorstore = Chroma.from_texts(
            texts=all_chunks,
            embedding=self.embeddings,
            metadatas=all_metadatas,
            persist_directory=chroma_store_path,
            collection_name="knowledge_base"
        )
        
        logger.info(f"Successfully built index with {len(all_chunks)} chunks from {len(pdf_files)} documents")

    def ensure_index_exists(self) -> bool:
        """Ensure the vector store exists, rebuild if necessary."""
        if self.vectorstore is None:
            logger.info("No vector store found, building index...")
            self.build_index()
            return True
        else:
            # Check if store has content
            try:
                # Try a simple search to verify the store works
                test_docs = self.vectorstore.similarity_search("test", k=1)
                logger.info(f"Vector store loaded successfully")
                return True 
            except Exception as e:
                logger.warning(f"Vector store exists but may be empty: {e}")
                self.build_index()
                return False

    def get_retriever(self, k: int = None):
        """Get a LangChain retriever for the vector store."""
        if self.vectorstore is None:
            self.ensure_index_exists()
        
        k = k or int(os.getenv("RETRIEVAL_K", "5"))
        return self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )
if __name__ == "__main__":
    # Test the RAG system
    rag = RAGSystem()
    rag.build_index()