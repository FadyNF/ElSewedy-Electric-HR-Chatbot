#!/usr/bin/env python3
"""
Simple script to clear the database.
"""

import os
import sys
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config.env")

def clear_database():
    """Clear only the document embeddings from the database."""
    db_config = {
        'host': os.getenv('PGHOST', 'localhost'),
        'port': int(os.getenv('PGPORT', '5433')),
        'database': os.getenv('PGDATABASE', 'test'),
        'user': os.getenv('PGUSER', 'postgres'),
        'password': os.getenv('PGPASSWORD', 'password')
    }
    
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as eng:
                # Clear only document embeddings
                eng.execute("DELETE FROM document_embeddings")
                print("Cleared document_embeddings table")
                
                conn.commit()
                print("Embeddings cleared successfully!")
                return True
    except Exception as e:
        print(f"Error clearing embeddings: {e}")
        return False

if __name__ == "__main__":
    clear_database() 