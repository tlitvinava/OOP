import datetime

class EditorSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EditorSettings, cls).__new__(cls)
            cls._instance.theme = "Светлая"
            cls._instance.font_size = 12
        return cls._instance

    def set_theme(self, theme):
        self.theme = theme

    def set_font_size(self, font_size):
        self.font_size = font_size

    def __str__(self):
        return f"Тема: {self.theme}, Размер шрифта: {self.font_size}"

class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.history = []
        return cls._instance

    def add_entry(self, document, user, action):
        entry = {
            "document": document,
            "user": user,
            "action": action,
            "timestamp": str(datetime.datetime.now())
        }
        self.history.append(entry)

    def view_history(self):
        return self.history
