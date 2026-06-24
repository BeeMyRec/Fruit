# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RentTracker
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "clients": clients,
        "items": items,
        "rentals": rentals,
        "deposits": deposits,
        "history": history
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
