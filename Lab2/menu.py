from text_editor import TextEditor, text_editor_menu
from document import DocumentManager
from user import User, get_user_role_for_document
from command import UndoCommand, RedoCommand
import user_manager 
from settings import EditorSettings, HistoryManager
from storage import LocalStorageStrategy, CloudStorageStrategy, SQLiteStorageStrategy

def save_document_in_storage(doc):
    print("\nВыберите способ сохранения документа:")
    print("1. Локально")
    print("2. В облако")
    print("3. В базу данных (SQLite)")
    choice = input("Введите номер выбора: ").strip()
    
    if choice == "1":
        strategy = LocalStorageStrategy()
    elif choice == "2":
        strategy = CloudStorageStrategy()
    elif choice == "3":
        strategy = SQLiteStorageStrategy()
    else:
        print("Неверный выбор, сохранение отменено.")
        return

    if choice in ["1", "2"]:
        print("Выберите формат файла:")
        print("1. TXT")
        print("2. JSON")
        print("3. XML")
        format_choice = input("Введите номер формата: ").strip()
        if format_choice == "1":
            format_type = "TXT"
        elif format_choice == "2":
            format_type = "JSON"
        elif format_choice == "3":
            format_type = "XML"
        else:
            print("Неверный выбор формата, сохранение отменено.")
            return
    else:
        format_type = None

    strategy.save(doc, format_type)


def settings_menu():
    settings = EditorSettings()
    history_manager = HistoryManager()
    while True:
        print("\n--- Настройки и персонализация ---")
        print("1. Изменить настройки редактора")
        print("2. Просмотреть историю изменений")
        print("3. Вернуться в главное меню")
        выбор = input("Выберите действие: ").strip()
        if выбор == "1":
            print(f"Текущие настройки: {settings}")
            новая_тема = input("Введите новую тему (например, Светлая/Тёмная): ").strip()
            if новая_тема:
                settings.set_theme(новая_тема)
            try:
                новый_размер = int(input("Введите новый размер шрифта (целое число): ").strip())
                settings.set_font_size(новый_размер)
            except ValueError:
                print("Неверный формат размера шрифта. Значение не изменено.")
            print("Обновлённые настройки:", settings)
        elif выбор == "2":
            история = history_manager.view_history()
            if история:
                print("\n--- История изменений ---")
                for entry in история:
                    print(f"{entry['timestamp']}: Документ '{entry['document']}' был {entry['action']} пользователем {entry['user']}")
            else:
                print("История пуста.")
        elif выбор == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def document_management_menu(doc_manager, active_user, users):
    while True:
        print("\n--- Меню управления документами ---")
        print("1. Создать документ")
        print("2. Открыть документ")
        print("3. Сохранить документ")
        print("4. Загрузить документ из файла")
        print("5. Удалить документ")
        print("6. Показать открытые документы")
        print("7. Вернуться в главное меню")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            title = input("Введите название документа: ").strip()
            print("Выберите тип документа:")
            print("1. PlainText")
            print("2. Markdown")
            print("3. RichText")
            doc_type_choice = input("Введите номер типа: ").strip()
            if doc_type_choice == "1":
                doc_type = "PlainText"
            elif doc_type_choice == "2":
                doc_type = "Markdown"
            elif doc_type_choice == "3":
                doc_type = "RichText"
            else:
                print("Неверный выбор типа документа.")
                continue

            active_user.documents.append({"title": title, "role": "admin"})
            for user in users:
                if user.username == active_user.username:
                    continue
                role_choice = input(
                    f"Введите роль для пользователя '{user.username}' (viewer/editor) или Enter для пропуска: "
                ).strip().lower()
                if role_choice in ["viewer", "editor"]:
                    user.documents.append({"title": title, "role": role_choice})
            doc = doc_manager.create_document(title, doc_type, owner=active_user)
            if doc:
                print(f"Документ '{title}' успешно создан с типом {doc_type}.")
        elif choice == "2":
            title = input("Введите название документа для открытия: ").strip()
            doc = doc_manager.open_document(title)
            if doc:
                role = None
                for entry in active_user.documents:
                    if entry.get("title") == doc.title:
                        role = entry.get("role")
                        break
                if role in ["editor", "admin"]:
                    if role == "admin":
                        doc_notifications = [note for note in active_user.notifications if doc.title in note]
                        if doc_notifications:
                            print(f"\nУ вас есть уведомления для документа '{doc.title}':")
                            for note in doc_notifications:
                                print(" -", note)
                            active_user.notifications = [note for note in active_user.notifications if doc.title not in note]
                    doc.is_open = True
                    print(f"Открытие документа '{doc.title}' в режиме редактирования...")
                    from text_editor import TextEditor, text_editor_menu
                    editor_instance = TextEditor()
                    editor_instance.content = doc.content  
                    text_editor_menu(editor_instance)
                    doc.edit(active_user, editor_instance.content)
                elif role == "viewer":
                    doc.is_open = True
                    print(f"Документ '{doc.title}' открыт в режиме только для чтения:")
                    print(doc.content)
                else:
                    print(f"У пользователя '{active_user.username}' нет доступа к документу '{doc.title}'.")
            else:
                print("Документ не найден.")
        elif choice == "3":
            title = input("Введите название документа для сохранения: ").strip()
            doc = doc_manager.open_document(title)
            if doc:
                save_document_in_storage(doc)
            else:
                print("Документ не найден.")
        elif choice == "4":
            file_path = input("Введите путь к файлу для загрузки: ").strip()
            try:
                from document import Document
                doc = Document.load(file_path)
                doc_manager.documents[doc.title] = doc
                print(f"Документ '{doc.title}' успешно загружен. Его контент:")
                print(doc.content)
            except Exception as e:
                print("Ошибка при загрузке документа:", e)
        elif choice == "5":
            title = input("Введите название документа для удаления: ").strip()
            doc_manager.delete_document(title)
        elif choice == "6":
            open_docs = [doc.title for doc in doc_manager.documents.values() if doc.is_open]
            if open_docs:
                print("\n--- Открытые документы ---")
                for title in open_docs:
                    print(title)
            else:
                print("Нет открытых документов.")
        elif choice == "7":
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")


def user_management_menu(users, doc_manager):
    while True:
        print("\n--- Меню управления пользователями ---")
        print("1. Создать нового пользователя")
        print("2. Показать список пользователей")
        print("3. Сохранить пользователей")
        print("4. Загрузить пользователей")
        print("5. Вернуться в главное меню")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            username = input("Введите имя нового пользователя: ").strip()
            if username:
                new_user = User(username)
                users.append(new_user)
                print(f"Пользователь '{username}' создан.")
            else:
                print("Имя пользователя не может быть пустым.")
        elif choice == "2":
            if users:
                print("\n--- Список пользователей ---")
                for user in users:
                    print(user)
            else:
                print("Список пользователей пуст.")
        elif choice == "3":
            user_manager.save_users(users)
        elif choice == "4":
            loaded_users, raw_data = user_manager.load_users()
            if loaded_users:
                users.clear()
                users.extend(loaded_users)
                print("Список пользователей обновлён из загруженных данных.")
            else:
                print("Нет сохранённых пользователей для загрузки.")
        elif choice == "5":
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

def main():
    doc_manager = DocumentManager()
    
    loaded_users, _ = user_manager.load_users()
    users = []
    if loaded_users:
        users.extend(loaded_users)
        active_user = users[0]
        print(f"Пользователи успешно загружены. Активный пользователь: {active_user.username}")
    else:
        print("Сохранённых пользователей не найдено.")
        while True:
            username = input("Введите имя первого пользователя: ").strip()
            if username:
                active_user = User(username)
                users.append(active_user)
                print(f"Пользователь '{active_user.username}' создан и назначен активным.")
                break
            else:
                print("Имя пользователя не может быть пустым. Пожалуйста, попробуйте снова.")
            
    while True:
        print("\n=== Консольный редактор документов ===")
        print("Активный пользователь:", active_user)
        print("1. Управление документами")
        print("2. Управление пользователями")
        print("3. Настройки и персонализация")
        print("4. Сменить активного пользователя")
        print("5. Выход из приложения")
        choice = input("Выберите номер действия: ").strip()

        if choice == "1":
            document_management_menu(doc_manager, active_user, users)
        elif choice == "2":
            user_management_menu(users, doc_manager)
        elif choice == "3":
            settings_menu()
        elif choice == "4":
            print("\n--- Выберите пользователя ---")
            for idx, user in enumerate(users):
                print(f"{idx + 1}. {user.username}")
            try:
                sel = int(input("Введите номер пользователя: ")) - 1
                if 0 <= sel < len(users):
                    active_user = users[sel]
                    print(f"Активный пользователь изменён на {active_user.username}.")
                else:
                    print("Неверный номер пользователя.")
            except ValueError:
                print("Некорректный ввод, ожидается число.")
        elif choice == "5":
            user_manager.save_users(users)
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
