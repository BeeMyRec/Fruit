# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RentTracker
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        # Валидация обязательных полей
        required_keys = ['clients', 'items', 'rentals']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует ключ {key}")
        
        # Преобразование типов, если нужно (например, даты)
        def normalize_date(d):
            return d if isinstance(d, str) else None
        
        normalized_data = {
            'clients': [{**c} for c in data.get('clients', [])],
            'items': [{**i} for i in data.get('items', [])],
            'rentals': [
                {
                    **r, 
                    'start_date': normalize_date(r.get('start_date')),
                    'end_date': normalize_date(r.get('end_date'))
                } 
                for r in data.get('rentals', [])
            ]
        }
        
        # Сохранение в переменную глобального состояния проекта (или файл)
        sys.modules['__main__'].RentTrackerState = normalized_data
        return normalized_data
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        raise

# Пример использования с данными из строки
initial_json_string = '''
{
  "clients": [
    {"id": 1, "name": "Иванов И.И.", "phone": "+79001234567"},
    {"id": 2, "name": "Петров П.П.", "phone": "+79007654321"}
  ],
  "items": [
    {"id": 101, "title": "Дрель", "category": "Инструменты"},
    {"id": 102, "title": "Велосипед", "category": "Транспорт"}
  ],
  "rentals": [
    {
      "client_id": 1, 
      "item_id": 101, 
      "start_date": "2023-10-01", 
      "end_date": "2023-10-05",
      "deposit_amount": 500.0,
      "status": "active"
    }
  ]
}'''

# Загрузка данных
try:
    RentTrackerState = load_initial_data(initial_json_string)
except Exception as e:
    print(f"Не удалось загрузить начальные данные: {e}")
    sys.exit(1)
