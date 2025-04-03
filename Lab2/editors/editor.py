from documents.plain_text import PlainText
from undo_redo.history import History
from undo_redo.text_command import TextCommand
import os

# class Editor:
#     def __init__(self, settings):
#         self.current_document = None
#         self.settings = settings
#         self.history = History()

#     def create_document(self, name):
#         self.current_document = PlainText(name)
#         print(f"Создан документ: {name}")

#     def open_document(self, name):
#         # Здесь можно добавить логику загрузки документа
#         print(f"Открыт документ: {name}")

#     def save_document(self, name):
#         if self.current_document:
#             self.current_document.save(LocalStorage())
#             print(f"Документ {name} сохранён.")
#         else:
#             print("Нет открытого документа.")

#     def add_text(self, text):
#         if self.current_document:
#             command = TextCommand(self.current_document, "add", text)
#             self.history.execute_command(command)
#             print(f"Добавлено: {text}")

#     def undo(self):
#         self.history.undo()
#         print("Отменено последнее действие.")

#     def redo(self):
#         self.history.redo()
#         print("Повторено последнее действие.")
from editors.text_operations import TextOperations
from editors.formatting import TextFormatter
from documents.document_factory import DocumentFactory


class Editor:
    def __init__(self, settings):
        self.current_document = None
        self.settings = settings
        self.history = History()
        self.text_operations = None

    def create_document(self, doc_type, name):
        self.current_document = DocumentFactory.create_document(doc_type, name)
        self.text_operations = TextOperations(self.current_document)  # Инициализация операций с текстом
        print(f"Создан документ: {name}")

    def add_text(self, text):
        if self.current_document:
            self.text_operations.insert_text(text)
            print(f"Добавлено: {text}")

    def apply_bold(self):
        if self.current_document:
            formatter = TextFormatter(self.current_document)
            formatter.apply_bold()
            print("Применено форматирование: жирный шрифт.")

    def cut_text(self, start, end):
        if self.current_document:
            self.text_operations.cut_text(start, end)
            print("Текст вырезан.")

    def copy_text(self, start, end):
        if self.current_document:
            self.text_operations.copy_text(start, end)
            print("Текст скопирован.")

    def paste_text(self):
        if self.current_document:
            self.text_operations.paste_text()
            print("Текст вставлен.")