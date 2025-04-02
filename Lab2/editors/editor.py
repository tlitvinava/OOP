from documents.plain_text import PlainText
from undo_redo.history import History
from undo_redo.text_command import TextCommand

class Editor:
    def __init__(self, settings):
        self.current_document = None
        self.settings = settings
        self.history = History()

    def create_document(self, name):
        self.current_document = PlainText(name)
        print(f"Создан документ: {name}")

    def open_document(self, name):
        # Здесь можно добавить логику загрузки документа
        print(f"Открыт документ: {name}")

    def save_document(self, name):
        if self.current_document:
            self.current_document.save(LocalStorage())
            print(f"Документ {name} сохранён.")
        else:
            print("Нет открытого документа.")

    def add_text(self, text):
        if self.current_document:
            command = TextCommand(self.current_document, "add", text)
            self.history.execute_command(command)
            print(f"Добавлено: {text}")

    def undo(self):
        self.history.undo()
        print("Отменено последнее действие.")

    def redo(self):
        self.history.redo()
        print("Повторено последнее действие.")