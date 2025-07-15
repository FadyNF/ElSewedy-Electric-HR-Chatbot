# import faiss
# import numpy as np
# import json

# # Load everything once
# index = faiss.read_index("data/embeddings/dress_code_policy.faiss")

# with open("data/embeddings/metadata.json", "r") as f:
#     metadata = json.load(f)

# def retrieve_chunks(query_embedding, top_k=3):
#     D, I = index.search(np.array([query_embedding]).astype("float32"), k=top_k)
#     return [metadata[i] for i in I[0]]


import sys
import os

sys.path.append(os.path.abspath(".."))

import numpy as np
from config.db_config import get_connection
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_chunks_from_db(query_text, top_k=5):
    query_vector = model.encode([query_text])[0].tolist()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT source_file, title, content, page_number
        FROM pdf_chunks
        ORDER BY embedding <-> %s::vector
        LIMIT %s;
    """,
        (query_vector, top_k),
    )

    rows = cursor.fetchall()
    conn.close()

    # Convert rows to chunks
    chunks = []
    for row in rows:
        chunks.append(
            {"source_file": row[0], "title": row[1], "content": row[2], "page": row[3]}
        )

    return chunks
