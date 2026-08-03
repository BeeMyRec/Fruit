# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RentTracker
def verify_and_repair_data():
    """Проверяет целостность данных аренды и автоматически исправляет простые проблемы."""
    issues = []
    
    # Проверка: все арендные записи должны иметь клиента, вещь, дату начала и дату возврата
    for record in rental_records:
        if not all([record.client_name, record.item_name, record.start_date, record.return_date]):
            issues.append(f"Запись {record.id} имеет неполные данные. Удалена.")
            rental_records.remove(record)
    
    # Проверка: даты должны быть валидными
    import datetime
    
    for record in rental_records:
        try:
            start = datetime.datetime.strptime(record.start_date, "%Y-%m-%d")
            return_dt = datetime.datetime.strptime(record.return_date, "%Y-%m-%d")
            
            if start > return_dt:
                issues.append(f"Запись {record.id}: дата возврата раньше даты начала. Исправлено.")
                record.return_date = (start + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
                
        except ValueError:
            issues.append(f"Запись {record.id} имеет невалидную дату. Удалена.")
            rental_records.remove(record)
    
    # Проверка: залог не должен превышать стоимость вещи (если есть данные об этом)
    for record in rental_records:
        if hasattr(record, 'item_cost') and hasattr(record, 'deposit_amount'):
            try:
                cost = float(record.item_cost)
                deposit = float(record.deposit_amount)
                if deposit > cost:
                    issues.append(f"Запись {record.id}: залог превышает стоимость вещи. Исправлено.")
                    record.deposit_amount = str(cost * 0.5)
            except (ValueError, TypeError):
                pass
    
    return issues
