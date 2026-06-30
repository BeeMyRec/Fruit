# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RentTracker
def generate_summary():
    if not data: return print("Данные пусты.")
    total_items = len(data.get('items', []))
    active_rentals = sum(1 for i in data['items'] if i['status'] == 'rented')
    overdue = [i for i in data['items'] if i['status'] == 'rented' and datetime.now() > datetime.fromisoformat(i.get('due_date', ''))]
    total_deposits = sum(i['deposit'] for i in data['items'])
    print(f"Всего вещей: {total_items}, Аренда активна: {active_rentals}, Просрочено: {len(overdue)}, Залоги всего: {total_deposits}")
