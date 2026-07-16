# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RentTracker
def show_rental(rental):
    """Вывод одной записи аренды в компактном формате."""
    print(f"ID: {rental['id']}")
    print(f"Вещь: {rental['item']}")
    print(f"Клиент: {rental['client_name']}")
    if rental.get('deposited'):
        print(f"Залог: {rental['deposit']} руб.")
    else:
        print("Залог: нет")
    if rental.get('returned'):
        print(f"Возвращено: {rental['return_date']}")
    else:
        print(f"Срок возврата: {rental['due_date']}")
