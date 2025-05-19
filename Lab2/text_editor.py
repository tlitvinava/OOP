from command import UndoCommand, RedoCommand

class TextEditor:
    def __init__(self):
        self.content = ""
        self.clipboard = ""
        self.history = []
        self.redo_stack = []

    def type_text(self, text):
        self.history.append(self.content)
        self.redo_stack.clear() 
        self.content += text

    def edit_text(self, new_content):
        self.history.append(self.content)
        self.redo_stack.clear()
        self.content = new_content

    def cut(self, start, end):
        self.clipboard = self.content[start:end]
        self.content = self.content[:start] + self.content[end:]
        self.history.append(self.content)
        self.redo_stack.clear()

    def copy(self, start, end):
        self.clipboard = self.content[start:end]

    def paste(self, position):
        self.history.append(self.content)
        self.redo_stack.clear()
        self.content = self.content[:position] + self.clipboard + self.content[position:]

    def search(self, word):
        positions = []
        start = 0
        while True:
            start = self.content.find(word, start)
            if start == -1:
                break
            positions.append(start)
            start += len(word)
        return positions

    def undo(self):
        if self.history:
            self.redo_stack.append(self.content) 
            self.content = self.history.pop()

    def redo(self):
        if self.redo_stack:
            self.history.append(self.content)  
            self.content = self.redo_stack.pop()

    def __str__(self):
        return self.content


class TextDecorator:
    def __init__(self, editor):
        self.editor = editor

    def bold(self):
        self.editor.content = f"**{self.editor.content}**"

    def italic(self):
        self.editor.content = f"*{self.editor.content}*"

    def underline(self):
        self.editor.content = f"__{self.editor.content}__"


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

# if __name__ == "__main__":
#     editor = TextEditor()

#     # Ввод текста
#     editor.type_text("Hello, World!")
#     print(editor)  # Output: Hello, World!

#     # Редактирование текста
#     editor.edit_text("Hello, Universe!")
#     print(editor)  # Output: Hello, Universe!

#     # Копирование, вырезание и вставка
#     editor.cut(7, 15)  # Вырезаем "Universe"
#     print(editor)  # Output: Hello, !
#     editor.paste(7)  # Вставляем "Universe" обратно
#     print(editor)  # Output: Hello, Universe!

#     # Поиск слова
#     positions = editor.search("Universe")
#     print("Positions of 'Universe':", positions)  # Output: Positions of 'Universe': [7]

#     # Форматирование текста
#     decorator = TextDecorator(editor)
#     decorator.bold()
#     print(editor)  # Output: **Hello, Universe!**
#     decorator.italic()
#     print(editor)  # Output: *Hello, Universe!*
#     decorator.underline()
#     print(editor)  # Output: __Hello, Universe!__

#     # Использование undo и redo
#     editor.undo()
#     print(editor)  # Output: **Hello, Universe!**
#     editor.redo()
#     print(editor)  # Output: *Hello, Universe!*