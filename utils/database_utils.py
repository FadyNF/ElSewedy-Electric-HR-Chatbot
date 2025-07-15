from config.db_config import get_connection


def create_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()

    # Table for text chunks
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pdf_chunks (
            id SERIAL PRIMARY KEY,
            source_file TEXT,
            title TEXT,
            content TEXT,
            page_number INT,
            embedding VECTOR(384)
        );
    """
    )

    # Table for image data with FK to section
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS image_chunks (
            id SERIAL PRIMARY KEY,
            chunk_id INTEGER REFERENCES pdf_chunks(id) ON DELETE CASCADE,
            image_path TEXT,
            ocr_text TEXT,
            embedding VECTOR(384)
        );
    """
    )

    conn.commit()
    conn.close()


# ⬇️ Returns section IDs so we can use them to link images later
def insert_sections_into_db(sections, embeddings):
    """
    sections: list of dicts (each with source_file, title, content, page)
    embeddings: list of numpy arrays (one per section)
    RETURNS: list of inserted section IDs (same order as sections)
    """
    conn = get_connection()
    cursor = conn.cursor()
    section_ids = []

    for section, embedding in zip(sections, embeddings):
        vector_str = "[" + ",".join(map(str, embedding)) + "]"

        cursor.execute(
            """
            INSERT INTO pdf_chunks (source_file, title, content, page_number, embedding)
            VALUES (%s, %s, %s, %s, %s::vector)
            RETURNING id
        """,
            (
                section.get("source_file", "Unknown"),
                section["title"],
                section["content"],
                section.get("page", 0),
                vector_str,
            ),
        )

        inserted_id = cursor.fetchone()[0]
        section_ids.append(inserted_id)

    conn.commit()
    conn.close()
    print("✅ All sections inserted into the database.")
    return section_ids


# ⬇️ Now using the foreign key from the section IDs
def insert_images_into_db(images, model):
    """
    images: list of dicts (must include 'chunk_id', 'image_path', 'ocr_text')
    model: sentence-transformers model
    """
    import numpy as np

    conn = get_connection()
    cursor = conn.cursor()

    for img in images:
        embedding = model.encode(img["ocr_text"]).astype("float32")
        vector_str = "[" + ",".join(map(str, embedding)) + "]"

        cursor.execute(
            """
            INSERT INTO image_chunks (chunk_id, image_path, ocr_text, embedding)
            VALUES (%s, %s, %s, %s::vector)
        """,
            (
                img["chunk_id"],
                img["image_path"],
                img["ocr_text"],
                vector_str,
            ),
        )

    conn.commit()
    conn.close()
    print("✅ All images inserted into the database.")
