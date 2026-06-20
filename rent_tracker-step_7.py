# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RentTracker
def sort_records(records, key='date'):
    if not records: return []
    order = {'date': 'desc', 'priority': 'asc', 'name': 'asc'}[key]
    reverse = (order == 'desc')
    def _sort_rec(r):
        v = r.get(key) or ''
        if key == 'date' and isinstance(v, str): return datetime.strptime(v, '%Y-%m-%d').timestamp()
        try: return int(float(v))
        except: return 0
    return sorted(records, key=_sort_rec, reverse=reverse)
