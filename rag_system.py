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
from documents import documents,metas
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


    def process_documents(self):
        """Process documents from the documents module"""
        self.policy_texts = []
        self.policy_metadata = []

        for policy_chunks, chunk_metadata in zip(documents, metas):
            # Join all chunks to one document
            joined_content = "\n\n".join(
                chunk["content"] if isinstance(chunk, dict) else str(chunk)
                for chunk in policy_chunks
            )

            self.policy_texts.append(joined_content)
            self.policy_metadata.append(chunk_metadata)

        logger.info(f"Extracted {len(self.policy_texts)} policy documents")
        for i, meta in enumerate(self.policy_metadata[:]):  # Show all
            print(f"{i+1}. {meta.get('policy_name', meta.get('form_name', 'Unknown'))}")

    def build_index(self, dir_path: Optional[str] = None):
        """Build the vector store index from processed documents"""
        # First process the documents
        self.process_documents()
        
        processed_documents = []
        processed_metadatas = []
        
        # Now embed  docs
        for text, metadata in zip(self.policy_texts, self.policy_metadata):
            if text and text.strip(): 
                # Convert keywords to string format for ChromaDB compatibility
                processed_metadata = metadata.copy()
                if 'keywords' in processed_metadata and isinstance(processed_metadata['keywords'], list):
                    processed_metadata['keywords'] = ", ".join(processed_metadata['keywords'])
                
                # Add content length and word count
                processed_metadata['content_length'] = len(text)
                processed_metadata['word_count'] = len(text.split())
                
                processed_documents.append(text)
                processed_metadatas.append(processed_metadata)
        
        if not processed_documents:
            logger.warning("No content extracted from any documents")
            return

        logger.info(f"Processing {len(processed_documents)} documents for embedding...")

        # Create vector store from all document chunks if it doesnt exist only.
        chroma_store_path = os.getenv("CHROMA_STORE_PATH")

        # if not chroma_store_path:
        self.vectorstore = Chroma.from_texts(
            texts=processed_documents,
            embedding=self.embeddings,
            metadatas=processed_metadatas,
            persist_directory=chroma_store_path,
            collection_name="knowledge_base"
        )
        logger.info(f"Successfully built index with {len(processed_documents)} document chunks")


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
                logger.info(f"Vector store loaded successfully with {len(test_docs)} documents found")
                return True 
            except Exception as e:
                logger.warning(f"Vector store exists but may be empty: {e}")
                self.build_index()
                return False

    def get_retriever(self, k: int = None):
        """Get a LangChain retriever for the vector store."""
        if self.vectorstore is None:
            self.ensure_index_exists()
        
        k = 1
        return self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )
if __name__ == "__main__":
    # Test the RAG system
    rag = RAGSystem()
    rag.build_index()
    print(f"\nSuccessfully embedded {len(rag.policy_texts)} documents!")