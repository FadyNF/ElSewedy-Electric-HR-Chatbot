from config.db_config import get_connection
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks_from_db(query_text, top_k=5):
    query_vector = model.encode([query_text])[0].tolist()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, source_file, title, content, page_number
        FROM pdf_chunks
        ORDER BY embedding <-> %s::vector
        LIMIT %s;
        """,
        (query_vector, top_k),
    )

    rows = cursor.fetchall()
    conn.close()

    chunks = []
    for row in rows:
        chunks.append({
            "id": row[0],
            "source_file": row[1],
            "title": row[2],
            "content": row[3],
            "page": row[4]
        })

    return chunks


def retrieve_relevant_images(query_text, top_k=3):
    query_vector = model.encode([query_text])[0].tolist()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT image_path, ocr_text, chunk_id
        FROM image_chunks
        ORDER BY embedding <-> %s::vector
        LIMIT %s;
        """,
        (query_vector, top_k),
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {"image_path": row[0], "ocr_text": row[1], "chunk_id": row[2]}
        for row in rows
    ]
