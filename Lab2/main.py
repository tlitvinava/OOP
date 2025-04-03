from settings.settings import Settings
from editors. editor import Editor
from users.user import User

# def main():
#     settings = Settings()
#     editor = Editor(settings)
#     user = User("admin", "admin", role="Admin")
    
#     while True:
#         command = input("\nВведите команду (create/open/save/add/undo/redo/exit): ").strip().lower()
#         if command == "create":
#             doc_name = input("Введите название документа: ")
#             editor.create_document(doc_name)
#         elif command == "open":
#             doc_name = input("Введите название документа для открытия: ")
#             editor.open_document(doc_name)
#         elif command == "save":
#             doc_name = input("Введите название документа для сохранения: ")
#             editor.save_document(doc_name)
#         elif command == "add":
#             text = input("Введите текст для добавления: ")
#             editor.add_text(text)
#         elif command == "undo":
#             editor.undo()
#         elif command == "redo":
#             editor.redo()
#         elif command == "exit":
#             break
#         else:
#             print("Неизвестная команда.")

def main():
    settings = Settings()
    editor = Editor(settings)
    user = User("admin", "admin", role="Admin")
    
    while True:
        command = input("\nВведите команду (create/add/cut/copy/paste/bold/exit): ").strip().lower()
        if command == "create":
            doc_type = input("Введите тип документа (plain/markdown/rich): ")
            doc_name = input("Введите название документа: ")
            editor.create_document(doc_type, doc_name)
        elif command == "add":
            text = input("Введите текст для добавления: ")
            editor.add_text(text)
        elif command == "cut":
            start = int(input("Введите начальный индекс для вырезания: "))
            end = int(input("Введите конечный индекс для вырезания: "))
            editor.cut_text(start, end)
        elif command == "copy":
            start = int(input("Введите начальный индекс для копирования: "))
            end = int(input("Введите конечный индекс для копирования: "))
            editor.copy_text(start, end)
        elif command == "paste":
            editor.paste_text()
        elif command == "bold":
            editor.apply_bold()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда.")