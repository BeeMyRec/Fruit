# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RentTracker
def print_metrics():
    metrics = {
        "Total clients": len(clients),
        "Active rentals": sum(1 for r in active_rentals if not r.is_returned),
        "Returned rentals": sum(1 for r in active_rentals if r.is_returned),
        "Pending returns": sum(1 for r in active_rentals if r.pending_return),
        "Total deposits collected": sum(r.deposit_amount for r in all_rentals),
        "Items rented out": len(set(item_id for r in all_rentals for item_id in [r.item_id])),
    }
    print("\n📊 RentTracker Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
