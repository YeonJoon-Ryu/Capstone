import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
import datetime

DB_PATH = Path(__file__).parent / "db" / "region_counts.db"

def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT timestamp, region_01, region_02 FROM region_counts ORDER BY timestamp")
    rows = cur.fetchall()
    conn.close()
    return rows

def main():
    rows = fetch_data()
    if not rows:
        print("DB에 데이터가 없습니다.")
        return

    # 시간, region-01, region-02 분리
    timestamps = [datetime.datetime.strptime(ts, "%Y%m%d_%H%M%S") for ts, _, _ in rows]
    region_01 = [r1 for _, r1, _ in rows]
    region_02 = [r2 for _, _, r2 in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, region_01, label="region-01", marker='o')
    plt.plot(timestamps, region_02, label="region-02", marker='o')
    plt.xlabel("시간")
    plt.ylabel("카운트")
    plt.title("시간대별 region-01, region-02 변화")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()