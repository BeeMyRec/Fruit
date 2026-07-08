# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RentTracker
def archive_completed_records(records, archive_folder='archive'):
    now = datetime.now()
    completed = [r for r in records if r.get('status') == 'completed']
    if not completed:
        print("Нет завершённых записей для архивации")
        return 0
    
    archived_count = 0
    with open(f'archive/{now.year}_{now.month}.txt', 'w') as f:
        for r in sorted(completed, key=lambda x: x.get('date_returned', ''), reverse=True):
            line_parts = [f"ID: {r['id']}", f"Дата аренды: {r['start_date']}", 
                          f"Дата возврата: {r['end_date']}", f"Статус: {r['status']}"]
            if 'client_name' in r:
                line_parts.append(f"Клиент: {r['client_name']}")
            if 'item_name' in r:
                line_parts.append(f"Предмет: {r['item_name']}")
            f.write('\n'.join(line_parts) + '\n')
            archived_count += 1
    
    print(f"Архивировано {archived_count} записей в {now.year}_{now.month}.txt")
    return archived_count
