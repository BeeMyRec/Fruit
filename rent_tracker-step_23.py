# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RentTracker
def print_table(title, rows):
    """Форматирует список кортежей (полей, значений) в таблицу."""
    if not rows:
        print(f"\nТаблица: {title}\n")
        return

    headers = [r[0] for r in rows]
    widths = [len(h) + 2 for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(val) > widths[i]:
                widths[i] = len(val)

    lines = []
    header_line = " | ".join(h.center(w) for h, w in zip(headers, widths))
    lines.append(header_line)
    sep = "-+-".join("-" * w for w in widths)
    lines.append(sep)
    for row in rows:
        line = " | ".join(str(v).ljust(w) for v, w in zip(row, widths))
        lines.append(line)

    print(f"\nТаблица: {title}")
    print("\n".join(lines))
