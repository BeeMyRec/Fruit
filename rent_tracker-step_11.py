# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RentTracker
import json, os, sys
DATA_FILE = "renttracker_data.json"
def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[Ошибка сохранения] {e}")

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        save_state({"clients": [], "rentals": [], "deposits": []})
