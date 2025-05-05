from command import UndoCommand, RedoCommand

class TextEditor:
    def __init__(self):
        self.content = ""
        self.clipboard = ""
        self.history = []
        self.redo_stack = []

    def type_text(self, text):
        self.history.append(self.content)
        self.redo_stack.clear()  # Очистка redo_stack при новом действии
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
            self.redo_stack.append(self.content)  # Сохраняем текущее состояние для redo
            self.content = self.history.pop()

    def redo(self):
        if self.redo_stack:
            self.history.append(self.content)  # Сохраняем текущее состояние для undo
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


# Пример использования
if __name__ == "__main__":
    editor = TextEditor()

    # Ввод текста
    editor.type_text("Hello, World!")
    print(editor)  # Output: Hello, World!

    # Редактирование текста
    editor.edit_text("Hello, Universe!")
    print(editor)  # Output: Hello, Universe!

    # Копирование, вырезание и вставка
    editor.cut(7, 15)  # Вырезаем "Universe"
    print(editor)  # Output: Hello, !
    editor.paste(7)  # Вставляем "Universe" обратно
    print(editor)  # Output: Hello, Universe!

    # Поиск слова
    positions = editor.search("Universe")
    print("Positions of 'Universe':", positions)  # Output: Positions of 'Universe': [7]

    # Форматирование текста
    decorator = TextDecorator(editor)
    decorator.bold()
    print(editor)  # Output: **Hello, Universe!**
    decorator.italic()
    print(editor)  # Output: *Hello, Universe!*
    decorator.underline()
    print(editor)  # Output: __Hello, Universe!__

    # Использование undo и redo
    editor.undo()
    print(editor)  # Output: **Hello, Universe!**
    editor.redo()
    print(editor)  # Output: *Hello, Universe!*