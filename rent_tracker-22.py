# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RentTracker
def check_overdue_notifications(db):
    """Возвращает список просроченных аренд, где срок возврата наступил."""
    overdue = []
    now = datetime.now()
    for rec in db["rentals"]:
        due_date_str = rec.get("due_date") or rec.get("returned_at")
        if not due_date_str:
            continue
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        except Exception:
            due_date = now
        if due_date <= now and rec.get("status") != "returned":
            overdue.append({
                "id": rec["id"],
                "item": rec.get("item"),
                "client": rec.get("client"),
                "due_date": due_date_str,
                "days_overdue": (now - due_date).days,
            })
    return overdue
