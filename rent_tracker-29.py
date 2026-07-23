# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: RentTracker
APP_CONFIG = {
    "app_name": "RentTracker",
    "version": "29",
    "rent_duration_days": 7,
    "deposit_percent": 15,
    "late_fee_day_rate": 0.5,
    "currency_symbol": "$",
    "max_items_per_client": 3,
}


def get_config(key: str):
    return APP_CONFIG.get(key)
