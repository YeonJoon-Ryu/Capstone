import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db" / "region_counts.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
for row in cur.execute("SELECT * FROM region_counts ORDER BY timestamp"):
    print(row)
conn.close()