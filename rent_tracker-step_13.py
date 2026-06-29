# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RentTracker
def search_rentals(query, fields=None):
    if not query: return []
    q = query.lower().strip()
    if fields is None: fields = ['client_name', 'item_name']
    results = [r for r in rentals if any(q in str(r.get(f, '')).lower() for f in fields)]
    return sorted(results, key=lambda x: (x['created_at'], x['status']))
