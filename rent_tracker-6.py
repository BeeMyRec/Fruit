# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RentTracker
def filter_records(query=None, status=None, category=None):
    if query:
        q = query.lower()
        records = [r for r in records if any(q in str(v).lower() for v in r.values())]
    if status:
        records = [r for r in records if r.get('status') == status]
    if category:
        records = [r for r in records if r.get('category') == category]
    return records
