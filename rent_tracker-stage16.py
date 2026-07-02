# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RentTracker
def generate_monthly_stats(records, start_date, end_date):
    from datetime import date
    stats = {}
    for r in records:
        if not isinstance(r['return_date'], str) and r['return_date']:
            d = r['return_date']
        elif isinstance(r['return_date'], str):
            try:
                d = date.fromisoformat(r['return_date'])
            except ValueError:
                continue
        else:
            continue
        if start_date <= d <= end_date:
            month_key = f"{d.year}-{d.month:02}"
            if month_key not in stats:
                stats[month_key] = {'total_rentals': 0, 'returned_items': [], 'overdue_count': 0}
            stats[month_key]['total_rentals'] += 1
            if r['return_date']:
                days_diff = (d - date.fromisoformat(r['rent_start_date'])).days if isinstance(r['rent_start_date'], str) else 0
                overdue_threshold = 30
                if d > date.fromisoformat(r['rent_start_date']) + timedelta(days=overdue_threshold):
                    stats[month_key]['overdue_count'] += 1
            stats[month_key]['returned_items'].append({
                'item': r['item_name'],
                'client': r['client_name'],
                'days_rented': days_diff,
                'deposit_refunded': r.get('deposit', 0) if not r.get('is_overdue') else 0
            })
    return stats
