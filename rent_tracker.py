# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RentTracker
import datetime

# Базовая структура данных: список клиентов и список активных аренд
clients = [
    {"id": 1, "name": "Иванов И.И.", "phone": "+79001234567"},
    {"id": 2, "name": "Петров П.П.", "phone": "+79007654321"}
]

rentals = [
    {"id": 1, "client_id": 1, "item": "Дрель", "date_from": datetime.date.today(), "due_date": datetime.date.today() + datetime.timedelta(days=7), "deposit": 500, "status": "active"},
    {"id": 2, "client_id": 2, "item": "Набор инструментов", "date_from": datetime.date.today() - datetime.timedelta(days=1), "due_date": datetime.date.today() + datetime.timedelta(days=3), "deposit": 1500, "status": "active"}
]

history = []

def log_event(action, details):
    history.append({"timestamp": datetime.datetime.now(), "action": action, "details": details})
    print(f"[{datetime.datetime.now().strftime('%H:%M')}] {action}: {details}")

def get_client_by_id(client_id):
    return next((c for c in clients if c["id"] == client_id), None)

def get_rental_by_id(rental_id):
    return next((r for r in rentals if r["id"] == rental_id), None)

print("RentTracker v0.1 инициализирован.")
log_event("START", "Запуск системы учета аренды")
