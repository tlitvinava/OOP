from text_editor import TextEditor, TextDecorator
from document import DocumentManager
from user import User
from command import UndoCommand, RedoCommand

def document_management_menu(doc_manager, active_user, users):
    while True:
        print("\n--- Меню управления документами ---")
        print("1. Создать документ")
        print("2. Открыть документ")
        print("3. Редактировать документ")
        print("4. Сохранить документ")
        print("5. Загрузить документ из файла")
        print("6. Удалить документ")
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

            print("Назначьте права доступа для пользователей:")
            print("(Оставьте поле пустым, если доступ не требуется)")
            # Здесь создаём список назначенных прав. Уже активный пользователь (владелец) получит роль "admin"
            permissions = {}
            for user in users:
                if user.username == active_user.username:
                    continue  # Пропускаем владельца, т.к. он уже имеет роль admin
                role_choice = input(f"Введите роль для пользователя '{user.username}' (viewer/editor) или Enter для пропуска: ").strip().lower()
                if role_choice in ["viewer", "editor"]:
                    permissions[user.username] = role_choice

            doc = doc_manager.create_document(title, doc_type, owner=active_user, permissions=permissions)
            if doc:
                print(f"Документ '{title}' успешно создан с типом {doc_type}.")
        elif choice == "2":
            title = input("Введите название документа для открытия: ").strip()
            doc = doc_manager.open_document(title)
            if doc:
                doc.open(active_user)
            else:
                print("Документ не найден.")
        elif choice == "3":
            title = input("Введите название документа для редактирования: ").strip()
            doc = doc_manager.open_document(title)
            if doc:
                new_content = input("Введите новый контент для документа: ")
                doc.edit(active_user, new_content)
            else:
                print("Документ не найден.")
        elif choice == "4":
            title = input("Введите название документа для сохранения: ").strip()
            doc = doc_manager.open_document(title)
            if doc:
                print("Выберите формат для сохранения:")
                print("1. TXT")
                print("2. JSON")
                print("3. XML")
                format_choice = input("Введите номер формата: ").strip()
                if format_choice == "1":
                    doc.save("TXT")
                    print("Документ сохранён в формате TXT.")
                elif format_choice == "2":
                    doc.save("JSON")
                    print("Документ сохранён в формате JSON.")
                elif format_choice == "3":
                    doc.save("XML")
                    print("Документ сохранён в формате XML.")
                else:
                    print("Неверный выбор формата.")
            else:
                print("Документ не найден.")
        elif choice == "5":
            file_path = input("Введите путь к файлу для загрузки: ").strip()
            try:
                # Здесь можно реализовать логику загрузки (по аналогии с Document.load)
                from document import Document
                doc = Document.load(file_path)
                doc_manager.documents[doc.title] = doc
                print(f"Документ '{doc.title}' успешно загружен. Его контент:")
                print(doc.content)
            except Exception as e:
                print("Ошибка при загрузке документа:", e)
        elif choice == "6":
            title = input("Введите название документа для удаления: ").strip()
            doc_manager.delete_document(title)
        elif choice == "7":
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

def text_editor_menu(editor):
    decorator = TextDecorator(editor)
    while True:
        print("\n--- Меню текстового редактора ---")
        print("1. Добавить текст")
        print("2. Редактировать текст")
        print("3. Вырезать текст")
        print("4. Копировать текст")
        print("5. Вставить текст")
        print("6. Поиск слова")
        print("7. Применить форматирование")
        print("8. Отменить действие (Undo)")
        print("9. Повторить действие (Redo)")
        print("10. Показать текущее содержимое")
        print("11. Вернуться в главное меню")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            text = input("Введите текст для добавления: ")
            editor.type_text(text)
            print("Текст добавлен.")
        elif choice == "2":
            new_content = input("Введите новый текст: ")
            editor.edit_text(new_content)
            print("Содержимое изменено.")
        elif choice == "3":
            try:
                start = int(input("Введите начальный индекс: "))
                end = int(input("Введите конечный индекс: "))
                editor.cut(start, end)
                print("Фрагмент вырезан.")
            except ValueError:
                print("Неверный ввод индексов.")
        elif choice == "4":
            try:
                start = int(input("Введите начальный индекс: "))
                end = int(input("Введите конечный индекс: "))
                editor.copy(start, end)
                print("Фрагмент скопирован.")
            except ValueError:
                print("Неверный ввод индексов.")
        elif choice == "5":
            try:
                position = int(input("Введите позицию для вставки: "))
                editor.paste(position)
                print("Фрагмент вставлен.")
            except ValueError:
                print("Неверный ввод индекса.")
        elif choice == "6":
            word = input("Введите слово для поиска: ")
            positions = editor.search(word)
            if positions:
                print("Слово найдено на позициях:", positions)
            else:
                print("Слово не найдено.")
        elif choice == "7":
            print("Выберите тип форматирования:")
            print("a. Жирный (Bold)")
            print("b. Курсив (Italic)")
            print("c. Подчёркивание (Underline)")
            style = input("Введите ваш выбор (a/b/c): ").strip().lower()
            if style == "a":
                decorator.bold()
                print("Применён жирный шрифт.")
            elif style == "b":
                decorator.italic()
                print("Применён курсив.")
            elif style == "c":
                decorator.underline()
                print("Применено подчёркивание.")
            else:
                print("Неверный выбор форматирования.")
        elif choice == "8":
            cmd = UndoCommand(editor)
            cmd.execute()
            print("Операция отменена.")
        elif choice == "9":
            cmd = RedoCommand(editor)
            cmd.execute()
            print("Операция повторена.")
        elif choice == "10":
            print("\n--- Текущее содержимое редактора ---")
            print(editor)
        elif choice == "11":
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

def user_management_menu(users):
    while True:
        print("\n--- Меню управления пользователями ---")
        print("1. Создать нового пользователя")
        print("2. Показать список пользователей")
        print("3. Вернуться в главное меню")
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
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

def main():
    doc_manager = DocumentManager()
    editor = TextEditor()  # объект текстового редактора
    users = []
    active_user = None

    # Создаём первого пользователя (администратора) – его создаём без роли, роль задается при создании документа.
    while not users:
        print("\nСоздайте первого пользователя:")
        username = input("Введите имя пользователя: ").strip()
        if username:
            user = User(username)
            users.append(user)
            active_user = user
            print(f"Пользователь '{user.username}' создан и назначен активным.")
        else:
            print("Имя пользователя не может быть пустым. Пожалуйста, попробуйте снова.")

    while True:
        print("\n=== Консольный редактор документов ===")
        print("Активный пользователь:", active_user)
        print("1. Управление документами")
        print("2. Текстовый редактор")
        print("3. Управление пользователями")
        print("4. Сменить активного пользователя")
        print("5. Выход из приложения")
        choice = input("Выберите номер действия: ").strip()

        if choice == "1":
            document_management_menu(doc_manager, active_user, users)
        elif choice == "2":
            text_editor_menu(editor)
        elif choice == "3":
            user_management_menu(users)
        elif choice == "4":
            print("\n--- Выберите пользователя ---")
            for idx, user in enumerate(users):
                print(f"{idx + 1}. {user.username}")
            try:
                sel = int(input("Введите номер пользователя для установки активного: ")) - 1
                if 0 <= sel < len(users):
                    active_user = users[sel]
                    print(f"Активный пользователь изменён на {active_user.username}.")
                else:
                    print("Неверный номер пользователя.")
            except ValueError:
                print("Некорректный ввод. Ожидается число.")
        elif choice == "5":
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()

