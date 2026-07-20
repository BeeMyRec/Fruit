# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RentTracker
def reset_demo_data():
    """Сбрасывает все данные к демо-состоянию."""
    global _rentals, _clients, _items, _deposits, _history
    
    _clients = [
        {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
        {"id": 2, "name": "Мария Петрова", "email": "maria@example.com"},
        {"id": 3, "name": "Алексей Сидоров", "email": "alex@example.com"}
    ]
    
    _items = [
        {"id": 1, "name": "Велосипед горный", "condition": "good"},
        {"id": 2, "name": "Фотоаппарат Canon EOS", "condition": "good"},
        {"id": 3, "name": "Тент для палатки", "condition": "fair"}
    ]
    
    _deposits = []
    
    _rentals = [
        {
            "id": 100, "item_id": 1, "client_id": 1, 
            "start_date": "2024-01-15", "end_date": "2024-02-15",
            "status": "active", "deposit": 3000, "notes": ""
        },
        {
            "id": 101, "item_id": 2, "client_id": 2, 
            "start_date": "2024-02-01", "end_date": "2024-03-01",
            "status": "active", "deposit": 5000, "notes": ""
        },
        {
            "id": 102, "item_id": 3, "client_id": 3, 
            "start_date": "2024-02-10", "end_date": "2024-02-25",
            "status": "active", "deposit": 1000, "notes": ""
        }
    ]
    
    _history = []

def clear_all_data():
    """Полностью очищает все данные."""
    global _rentals, _clients, _items, _deposits, _history
    
    _clients = []
    _items = []
    _deposits = []
    _rentals = []
    _history = []

def init_demo_data():
    """Инициализирует демо-данные при первом запуске."""
    global _rentals, _clients, _items, _deposits, _history
    
    if not _clients:
        reset_demo_data()
