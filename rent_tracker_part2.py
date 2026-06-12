# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RentTracker
class ValidationError(Exception): pass

def validate_client(name: str, phone: str) -> dict:
    if not name or len(name.strip()) < 2: raise ValidationError("Имя клиента должно быть непустым и содержать минимум 2 символа.")
    if not re.match(r"^\+?[0-9\-\(\)\s]{10,}$", phone): raise ValidationError("Неверный формат телефона.")
    return {"id": uuid.uuid4().hex[:8], "name": name.strip(), "phone": phone}

def validate_item(name: str, category: str) -> dict:
    if not name or len(name.strip()) < 2: raise ValidationError("Название вещи должно быть непустым и содержать минимум 2 символа.")
    allowed_categories = ["Электроника", "Инструменты", "Одежда", "Мебель", "Другое"]
    if category not in allowed_categories: raise ValidationError(f"Категория должна быть одной из: {', '.join(allowed_categories)}")
    return {"id": uuid.uuid4().hex[:8], "name": name.strip(), "category": category}

def validate_rental(client_id: str, item_id: str, due_date: str) -> dict:
    if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", due_date): raise ValidationError("Дата возврата должна быть в формате ДД.ММ.ГГГГ.")
    return {"id": uuid.uuid4().hex[:8], "client_id": client_id, "item_id": item_id, "due_date": due_date}

def validate_deposit(amount: float) -> dict:
    if amount < 0 or amount > 100000: raise ValidationError("Залог должен быть неотрицательным числом и не превышать 100 000.")
    return {"id": uuid.uuid4().hex[:8], "amount": round(amount, 2)}

def validate_return(rental_id: str, deposit_id: str) -> dict:
    if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", due_date): raise ValidationError("Дата возврата должна быть в формате ДД.ММ.ГГГГ.")
    return {"id": uuid.uuid4().hex[:8], "rental_id": rental_id, "deposit_id": deposit_id}
