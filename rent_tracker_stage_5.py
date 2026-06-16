# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RentTracker
def delete_rental(record_id: int) -> bool:
    """Удалить запись аренды по ID, безопасно обрабатывая отсутствующий идентификатор."""
    if record_id not in rentals_db:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    deleted_record = rentals_db.pop(record_id)
    
    # Обновляем историю операций для удалённой записи (опционально, если требуется аудит)
    if 'history' not in deleted_record:
        deleted_record['history'] = []
    deleted_record['history'].append({
        "action": "deleted",
        "timestamp": datetime.now().isoformat(),
        "reason": f"Удаление записи аренды по ID {record_id}"
    })
    
    print(f"Запись с ID {record_id} успешно удалена.")
    return True
