# === Stage 32: Добавь журнал действий пользователя ===
# Project: RentTracker
class UserActionLog:
    def __init__(self):
        self.actions = []
    
    def log(self, action_type, item_name, user_name=None, details=""):
        self.actions.append({
            "type": action_type,
            "item": item_name,
            "user": user_name or "system",
            "details": details,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def get_recent(self, limit=10):
        return self.actions[-limit:]
    
    def search_actions(self, keyword):
        return [a for a in self.actions if keyword.lower() in str(a).lower()]

# Пример использования:
log = UserActionLog()
log.log("rented", "Дрон DJI Mini", user_name="Иван Иванов", details="Период: 2024-01-15 до 2024-02-15")
log.log("returned", "Ноутбук MacBook Pro", user_name="Петр Петров", details="Возвращен без повреждений")

print(f"Последние действия: {len(log.get_recent())}")
for action in log.search_actions("Иван"):
    print(f"- [{action['type']}] {action['item']} (пользователь: {action['user']})")
