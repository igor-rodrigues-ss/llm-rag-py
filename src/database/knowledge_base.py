from src.model import embed

from src.database.setup import connect


def insert(page_number: int, text: str):
    embeddings = embed.text_to_embeddings(text)

    with connect() as cursor:
        cursor.execute(
            "INSERT INTO items (page_number, content, embedding) VALUES (%s, %s, %s)",
            (page_number, text, embeddings),
        )


def query_context_by_similarity(text: str, limit: int = 5) -> list:
    embeddings = embed.text_to_embeddings(text)

    with connect() as cursor:
        cursor.execute(
            """
            SELECT "content", 1 - (embedding <=> %s::vector) as similarity
            FROM items
            where 1 - (embedding <=> %s::vector) > 0.3
            ORDER BY similarity DESC
            LIMIT %s
            """,
            (embeddings, embeddings, limit),
        )

        results = cursor.fetchall()

    return results
