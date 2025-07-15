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

    # Table for image data
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS image_chunks (
            id SERIAL PRIMARY KEY,
            source_file TEXT,
            page_number INT,
            image_path TEXT,
            ocr_text TEXT,
            embedding VECTOR(384),
            linked_section_title TEXT
        );
    """
    )

    conn.commit()
    conn.close()


def insert_sections_into_db(sections, embeddings):
    """
    sections: list of dicts (each with source_file, title, content, page)
    embeddings: list of numpy arrays (one per section)
    """
    conn = get_connection()
    cursor = conn.cursor()

    for section, embedding in zip(sections, embeddings):
        # Ensure it's a 1D list of strings for SQL insertion
        vector_str = "[" + ",".join(map(str, embedding)) + "]"

        cursor.execute(
            """
            INSERT INTO pdf_chunks (source_file, title, content, page_number, embedding)
            VALUES (%s, %s, %s, %s, %s::vector)
        """,
            (
                section.get("source_file", "Unknown"),
                section["title"],
                section["content"],
                section.get("page", 0),
                vector_str,
            ),
        )

    conn.commit()
    conn.close()
    print("✅ All sections inserted into the database.")


def insert_images_into_db(images, model):
    """
    images: list of dicts (each with image_path, ocr_text, linked_section_title, page)
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
            INSERT INTO image_chunks (source_file, page_number, image_path, ocr_text, embedding, linked_section_title)
            VALUES (%s, %s, %s, %s, %s::vector, %s)
        """,
            (
                img.get("source_file", "Unknown"),
                img.get("page", 0),
                img.get("image_path"),
                img.get("ocr_text"),
                vector_str,
                img.get("linked_section_title", "Unknown"),
            ),
        )

    conn.commit()
    conn.close()
    print("✅ All images inserted into the database.")
