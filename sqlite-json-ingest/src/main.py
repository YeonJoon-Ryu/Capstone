import json
from pathlib import Path
from db import database

def extract_timestamp(filename: str) -> str:
    # 파일명에서 result_와 .json을 제거
    return filename.replace("result_", "").replace(".json", "")

def main():
    data_dir = Path(__file__).parent / "data"
    database.create_table()

    for json_file in sorted(data_dir.glob("result_*.json")):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        timestamp = extract_timestamp(json_file.name)
        region_01 = data["region_counts"]["region-01"]
        region_02 = data["region_counts"]["region-02"]
        database.insert_region_count(timestamp, region_01, region_02)
        print(f"{timestamp}: region-01={region_01}, region-02={region_02} 저장 완료")

if __name__ == "__main__":
    main()