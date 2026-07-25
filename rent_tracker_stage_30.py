# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RentTracker
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"{self.name} ({self.email})"
