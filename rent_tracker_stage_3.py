# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RentTracker
class RentTracker:
    def __init__(self):
        self._records = []
    
    def add_rental(self, item_name, client_name, start_date, end_date, deposit=0):
        record = {
            "id": len(self._records) + 1,
            "item": item_name,
            "client": client_name,
            "start": start_date,
            "end": end_date,
            "deposit": deposit,
            "status": "active" if int(end_date.replace("-", "")) > int(start_date.replace("-", "")) else "expired",
            "history": []
        }
        self._records.append(record)
        return record
    
    def get_records(self):
        return list(self._records)
