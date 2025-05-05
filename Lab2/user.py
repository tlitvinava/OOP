from document import Document

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # 'admin', 'editor', 'viewer'
        self.observers = []

    def can_edit(self):
        return self.role in ['admin', 'editor']

    def can_view(self):
        return self.role in ['admin', 'editor', 'viewer']

    def change_role(self, new_role):
        self.role = new_role
        self.notify_observers()

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"
    



if __name__ == "__main__":
    # Создание пользователей
    admin = User("Alice", "admin")
    editor = User("Bob", "editor")
    viewer = User("Charlie", "viewer")

    # Создание документа
    doc = Document("My Document")

    # Открытие документа
    doc.open(viewer)  # Charlie открывает в read-only
    doc.open(editor)  # Bob открывает в editable
    doc.open(admin)   # Alice открывает в editable

    # Редактирование документа
    doc.edit(editor, "New content by Bob.")
    print(doc)  # Проверка контента документа

    # Попытка редактирования.viewer
    doc.edit(viewer, "Attempt to change content.")  # Charlie не может редактировать

    # Изменение роли
    admin.change_role("viewer")  # Alice становится viewer
    print(admin)  # Проверка новой роли