# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RentTracker
def switch_user_profile(new_name):
    if new_name not in profiles:
        print(f"Профиль '{new_name}' не найден.")
        return False
    active_id = next((p["id"] for p in profiles if p["name"] == new_name), None)
    if active_id is None:
        return False
    active_user["id"] = active_id
    active_user["name"] = new_name
    print(f"Переключение на профиль: {new_name}")
    return True
