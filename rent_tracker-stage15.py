# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RentTracker
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    dates = sorted(set(r['return_date'] for r in records))
    stats = {}
    for d in dates:
        week_start = (d - timedelta(days=d.weekday())).date()
        week_end = week_start + timedelta(weeks=1) - timedelta(days=1)
        key = f"{week_start.isoformat()}_{week_end.isoformat()}"
        stats[key] = {
            'total_rentals': sum(1 for r in records if week_start <= date.fromisoformat(r['return_date']) <= week_end),
            'avg_duration': sum((date.fromisoformat(r['return_date']) - date.fromisoformat(r['rent_date'])).days for r in records if week_start <= date.fromisoformat(r['return_date']) <= week_end) / max(1, sum(1 for r in records if week_start <= date.fromisoformat(r['return_date']) <= week_end)),
            'total_deposit': sum(float(r.get('deposit', 0)) for r in records if week_start <= date.fromisoformat(r['return_date']) <= week_end)
        }
    return stats
