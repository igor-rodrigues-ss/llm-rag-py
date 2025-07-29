import psycopg2

from contextlib import contextmanager

from src.config import DATABASE_URL


@contextmanager
def connect():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    yield cursor

    conn.commit()
    cursor.close()
    conn.close()
