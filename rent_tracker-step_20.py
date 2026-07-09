# === Stage 20: Добавь восстановление записей из архива ===
# Project: RentTracker
def load_from_archive(self, archive_path):
        """Восстанавливает записи из текстового архива в формате:
        <id>|<client_id>|<item_name>|<rent_date>|<return_date>|<deposit>|<status>"""
        if not os.path.exists(archive_path):
            return 0
        count = 0
        with open(archive_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split('|')
                if len(parts) != 7:
                    continue
                try:
                    rec_id, client_id, item_name, rent_date, return_date, deposit_str, status = (
                        int(p.strip()) for p in parts[:6] + [p.strip()]
                    )
                except ValueError:
                    continue
                if self.get_record(rec_id) is not None:
                    continue
                client = self.clients.get(client_id)
                if client is None:
                    continue
                new_rec = Record(
                    id=rec_id,
                    client_id=client_id,
                    item_name=item_name,
                    rent_date=datetime.strptime(rent_date[:10], '%Y-%m-%d') if len(rent_date) >= 10 else datetime.now(),
                    return_date=datetime.strptime(return_date[:10], '%Y-%m-%d') if len(return_date) >= 10 else None,
                    deposit=deposit_str,
                    status=status.lower()
                )
                self.records[rec_id] = new_rec
                count += 1
        print(f"[RentTracker] Восстановлено {count} записей из архива: {archive_path}")
        return count
