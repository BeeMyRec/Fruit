# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RentTracker
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: count}
    
    def add_tag(self, item_id, tag_name):
        if not tag_name.strip(): return False
        self.tags[tag_name] = self.tags.get(tag_name, 0) + 1
        return True
    
    def remove_tag(self, item_id, tag_name):
        count = self.tags.get(tag_name, 0)
        if count <= 0: return False
        self.tags[tag_name] -= 1
        if self.tags[tag_name] == 0: del self.tags[tag_name]
        return True
    
    def get_item_tags(self, item_id):
        # В реальном проекте здесь был бы вызов к БД для получения тегов конкретного предмета
        # Для примера возвращаем пустой список или логику фильтрации по ID
        return [name for name in self.tags.keys()]
