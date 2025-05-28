import time
import json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db import database

DATA_DIR = Path(__file__).parent / "data"

class NewJsonHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".json"):
            return
        json_file = Path(event.src_path)
        if json_file.name.startswith("result_"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                timestamp = json_file.stem.replace("result_", "")
                region_01 = data["region_counts"]["region-01"]
                region_02 = data["region_counts"]["region-02"]
                database.insert_region_count(timestamp, region_01, region_02)
                print(f"{timestamp}: region-01={region_01}, region-02={region_02} 저장 완료")
            except Exception as e:
                print(f"{json_file.name} 처리 중 오류 발생: {e}")

def main():
    database.create_table()
    event_handler = NewJsonHandler()
    observer = Observer()
    observer.schedule(event_handler, str(DATA_DIR), recursive=False)
    observer.start()
    print("폴더 감시 시작! (Ctrl+C로 종료)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()