import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "region_counts.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS region_counts (
                timestamp TEXT PRIMARY KEY,
                region_01 INTEGER,
                region_02 INTEGER
            )
        """)
        conn.commit()

def insert_region_count(timestamp: str, region_01: int, region_02: int):
    with get_connection() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO region_counts (timestamp, region_01, region_02) VALUES (?, ?, ?)",
            (timestamp, region_01, region_02)
        )
        conn.commit()