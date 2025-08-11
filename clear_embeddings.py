#!/usr/bin/env python3
"""
Clear the ChromaDB collection used for embeddings.
"""

import os
from dotenv import load_dotenv
import chromadb

# Load environment variables
load_dotenv("config.env")

def clear_chroma_collection():
    """Drop or empty the 'knowledge_base' collection in ChromaDB."""
    chroma_store_path = os.getenv("CHROMA_STORE_PATH", os.path.join(os.getcwd(), "chroma_store"))
    client = chromadb.PersistentClient(path=chroma_store_path)
    collection_name = "knowledge_base"
    try:
        # Prefer dropping the collection for a clean reset
        names = [c.name for c in client.list_collections()]
        if collection_name in names:
            client.delete_collection(collection_name)
            print(f"Dropped collection: {collection_name}")
        else:
            print(f"Collection '{collection_name}' not found; nothing to clear.")
        return True
    except Exception as e:
        print(f"Error clearing Chroma collection: {e}")
        return False

if __name__ == "__main__":
    clear_chroma_collection()