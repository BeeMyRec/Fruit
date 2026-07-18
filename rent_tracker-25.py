# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RentTracker
class BadDateError(Exception):
    pass


def parse_date(date_str: str) -> datetime.date:
    """Парсит дату в формате YYYY-MM-DD, возвращает date."""
    if not isinstance(date_str, str):
        raise BadDateError(f"Дата должна быть строкой, получено {type(date_str).__name__}")
    
    parts = date_str.strip().split('-')
    if len(parts) != 3:
        raise BadDateError(f"Неверный формат даты: '{date_str}' (ожидалось YYYY-MM-DD)")

    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    
    try:
        return datetime.date(year, month, day)
    except ValueError as e:
        raise BadDateError(f"Некорректная дата '{date_str}': {e}")


def to_iso_date(d: datetime.date) -> str:
    """Форматирует date в YYYY-MM-DD."""
    return d.strftime('%Y-%m-%d')
