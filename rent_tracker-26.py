# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RentTracker
def demo_run():
    """Ручной демо-набор команд для быстрого тестирования."""
    db = Database()

    # Создаём клиентов
    client1 = Client(name="Иван Иванов", phone="+79001234567")
    client2 = Client(name="Мария Петрова", phone="+79007654321")
    db.add_client(client1)
    db.add_client(client2)

    # Создаём вещи
    item1 = Item(name="Велосипед", owner="Склад", condition="Отличный")
    item2 = Item(name="Фотоаппарат", owner="Склад", condition="Хороший")
    db.add_item(item1)
    db.add_item(item2)

    # Создаём арендодателя (организацию)
    org = Organization(name="РентКомплект", phone="+79001112233")
    db.add_organization(org)

    print("=== Демо-клиенты ===")
    for c in db.get_all_clients():
        print(f"  {c.name} — {c.phone}")

    print("\n=== Демо-вещи ===")
    for i in db.get_all_items():
        print(f"  {i.name} (условие: {i.condition})")

    print("\n=== Демо-аренда ===")
    rent = Rent(
        item=item1, client=client1, organization=org,
        start_date="2025-10-01", end_date="2025-11-01",
        deposit=3000, price_per_day=500, status="active"
    )
    db.add_rent(rent)
    print(f"  Аренда: {rent.item.name} → {rent.client.name}, статус={rent.status}")

    print("\n=== Демо-возврат ===")
    return_event = ReturnEvent(
        rent_id=rent.id, date="2025-11-05", status="completed"
    )
    db.add_return(return_event)
    print(f"  Возврат #{return_event.id}: статус={return_event.status}")

    # Показываем итоговую историю
    history = History()
    for event in [rent, return_event]:
        history.append(event)
    print("\n=== История ===")
    for h in history:
        print(f"  {h.__class__.__name__}: {h}")

    # Показываем все сущности для проверки
    print("\n=== База данных (проверка) ===")
    print(f"  Клиентов: {db.get_all_clients_count()}")
    print(f"  Вещей: {db.get_all_items_count()}")
    print(f"  Организаций: {db.get_all_organizations_count()}")
    print(f"  Аренд: {db.get_all_rents_count()}")
