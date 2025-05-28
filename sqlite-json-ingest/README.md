# SQLite JSON Ingest

Jetson에서 시간대별로 생성되는 JSON 파일의 region 정보를 SQLite 데이터베이스에 자동으로 저장하는 프로젝트입니다.

## 폴더 구조
sqlite-json-ingest/ ├─ src/ │ ├─ main.py │ ├─ watch_and_ingest.py │ ├─ show_db.py │ ├─ visualize.py │ ├─ db/ │ │ └─ database.py │ └─ data/ │ └─ (result_*.json 파일들이 저장되는 폴더) ├─ requirements.txt └─

## 주요 기능

- **JSON → SQLite 자동 저장:**  
  `src/data` 폴더에 새로운 JSON 파일이 생성될 때마다 region 정보를 DB에 자동 저장

- **DB 데이터 확인:**  
  `show_db.py`로 DB에 저장된 데이터를 터미널에서 확인

- **DB 시각화:**  
  `visualize.py`로 시간대별 region 변화를 그래프로 확인

## 설치 및 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 폴더 감시 및 자동 저장 실행

```bash
cd src
python watch_and_ingest.py
```
src/data 폴더에 새로운 result_*.json 파일이 추가되면 자동으로 DB에 저장됩니다.

### 3. DB 데이터 확인

```bash
python show_db.py
```

### 4.DB 시각화

```bash
python visualize.py
```

### 참고
 - JSON 파일명 예시: result_20250527_220708.json
 - JSON 구조 예시:
``` bash
{
  "region_counts": {
    "region-01": 27,
    "region-02": 8
  }
}
```