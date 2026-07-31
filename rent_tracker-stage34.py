# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RentTracker
TEMPLATES = {
    "camera": {"name": "Камера", "rent_days": 5, "deposit": 1000},
    "drill": {"name": "Дрель", "rent_days": 2, "deposit": 300},
    "projector": {"name": "Проектор", "rent_days": 3, "deposit": 800},
}

def fill_from_template(record, tpl_name):
    if tpl_name not in TEMPLATES:
        raise ValueError(f"Нет шаблона '{tpl_name}'. Доступные: {list(TEMPLATES)}")
    for key, val in TEMPLATES[tpl_name].items():
        record[key] = val
