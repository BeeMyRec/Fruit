# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RentTracker
def show_menu():
    print("\n=== Меню RentTracker ===")
    print("1. Список всех аренд")
    print("2. Статус клиента (залог)")
    print("3. История операций")
    print("4. Выход")
    choice = input("Выберите действие: ").strip()
    if choice == "1":
        for r in rentals:
            print(f"{r['id']}: {r['item']} -> {r['client']['name']} (до {r['return_date']})")
    elif choice == "2":
        name = input("Имя клиента: ")
        client = next((c for c in clients if c['name'].lower() == name.lower()), None)
        if client:
            print(f"Клиент: {client['name']}, Залог: {client.get('deposit', 0)} руб.")
    elif choice == "3":
        history = [h for r in rentals for h in r.get('history', [])]
        for h in sorted(history, key=lambda x: x['date'], reverse=True):
            print(f"{h['date']}: {h['action']}")
    else:
        exit()
