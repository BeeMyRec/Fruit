# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RentTracker
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date  # datetime.date или str в формате 'YYYY-MM-DD'

    @property
    def is_overdue(self):
        if isinstance(self.due_date, str):
            due = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        else:
            due = self.due_date
        return due < datetime.now().date()

    def __str__(self):
        status = "ПЕРЕДИ СРОКОМ" if self.is_overdue else "В срок"
        return f"[{status}] {self.title} — до {self.due_date}"


reminders = []

def add_reminder(title, due_date_str=""):
    reminders.append(Reminder(title, due_date_str))
    print(f"Напоминание добавлено: '{title}'")

def show_reminders():
    if not reminders:
        print("Нет напоминаний.")
        return
    for r in sorted(reminders, key=lambda x: str(x.due_date)):
        print(r)
