# import json
# import os
# import dicttoxml
# from xml.etree import ElementTree as ET

# class Document:
#     def __init__(self, title, content="", doc_type="PlainText"):
#         self.title = title
#         self.content = content
#         self.doc_type = doc_type

#     def open(self, user):
#         if user.can_view():
#             self.read_only = not user.can_edit()
#             mode = "read-only" if self.read_only else "editable"
#             print(f"{user.username} opened '{self.title}' in {mode} mode.")
#         else:
#             print(f"{user.username} does not have permission to view '{self.title}'.")

#     def edit(self, user, new_content):
#         if user.can_edit():
#             self.content = new_content
#             print(f"{user.username} edited '{self.title}'.")
#         else:
#             print(f"{user.username} does not have permission to edit '{self.title}'.")

#     def save(self, format_type):
#         if format_type == "TXT":
#             with open(f"{self.title}.txt", "w", encoding="utf-8") as file:
#                 file.write(self.content)
#         elif format_type == "JSON":
#             with open(f"{self.title}.json", "w", encoding="utf-8") as file:
#                 json.dump({"title": self.title, "content": self.content}, file)
#         elif format_type == "XML":
#             xml_content = dicttoxml.dicttoxml({"title": self.title, "content": self.content})
#             with open(f"{self.title}.xml", "wb") as file:
#                 file.write(xml_content)
#         else:
#             print("Unsupported format.")

#     @classmethod
#     def load(cls, file_path):
#         if file_path.endswith('.txt'):
#             with open(file_path, 'r', encoding="utf-8") as file:
#                 content = file.read()
#                 return cls(title=os.path.basename(file_path).replace('.txt', ''), content=content)
#         elif file_path.endswith('.json'):
#             with open(file_path, 'r', encoding="utf-8") as file:
#                 data = json.load(file)
#                 return cls(title=data['title'], content=data['content'], doc_type="JSON")
#         elif file_path.endswith('.xml'):
#             with open(file_path, 'rb') as file:
#                 data = ET.parse(file).getroot()
#                 title = data.find('title').text
#                 content = data.find('content').text
#                 return cls(title=title, content=content, doc_type="XML")
#         else:
#             raise ValueError("Unsupported file format")

#     def delete(self):
#         try:
#             os.remove(f"{self.title}.txt")
#             os.remove(f"{self.title}.json")
#             os.remove(f"{self.title}.xml")
#         except FileNotFoundError:
#             print(f"File(s) for document '{self.title}' do not exist.")


# # Специфические типы документов:

# class PlainTextDocument(Document):
#     def __init__(self, title, content=""):
#         super().__init__(title, content, doc_type="PlainText")
#         # Здесь можно добавить специфичную логику для PlainText

# class MarkdownDocument(Document):
#     def __init__(self, title, content=""):
#         super().__init__(title, content, doc_type="Markdown")
#         # Добавьте здесь методы для конвертации Markdown или специфичное форматирование

# class RichTextDocument(Document):
#     def __init__(self, title, content=""):
#         super().__init__(title, content, doc_type="RichText")
#         # Дополнительные свойства (например, стили и форматирование) можно добавить здесь


# # Фабрика для создания документов

# class DocumentFactory:
#     @staticmethod
#     def create_document(doc_type, title, content=""):
#         if doc_type == "PlainText":
#             return PlainTextDocument(title, content)
#         elif doc_type == "Markdown":
#             return MarkdownDocument(title, content)
#         elif doc_type == "RichText":
#             return RichTextDocument(title, content)
#         else:
#             raise ValueError(f"Unsupported document type: {doc_type}")


# # Обновленный класс DocumentManager, который теперь использует фабрику

# class DocumentManager:
#     def __init__(self):
#         self.documents = {}

#     def create_document(self, title, doc_type="PlainText"):
#         if title in self.documents:
#             print("Document already exists.")
#             return None
#         doc = DocumentFactory.create_document(doc_type, title)
#         self.documents[title] = doc
#         return doc

#     def open_document(self, title):
#         return self.documents.get(title)

#     def delete_document(self, title):
#         if title in self.documents:
#             self.documents[title].delete()
#             del self.documents[title]
#             print(f"Document '{title}' deleted.")
#         else:
#             print("Document not found.")

# document.py

import json
import os
import dicttoxml
from xml.etree import ElementTree as ET

class Document:
    def __init__(self, title, content="", doc_type="PlainText", owner=None):
        self.title = title
        self.content = content
        self.doc_type = doc_type
        self.owner = owner  # пользователь, создавший документ
        self.permissions = {}  # словарь: username -> role ("admin", "editor", "viewer")
        if owner:
            # Владелец документа автоматически получает права администратора для данного документа
            self.permissions[owner.username] = "admin"

    def open(self, user):
        role = self.permissions.get(user.username)
        if role in ["viewer", "editor", "admin"]:
            read_only = (role == "viewer")
            mode = "read-only" if read_only else "editable"
            print(f"Пользователь '{user.username}' открыл документ '{self.title}' в режиме {mode}.")
        else:
            print(f"У пользователя '{user.username}' нет доступа к документу '{self.title}'.")

    def edit(self, user, new_content):
        role = self.permissions.get(user.username)
        if role in ["editor", "admin"]:
            self.content = new_content
            print(f"Пользователь '{user.username}' отредактировал документ '{self.title}'.")
        else:
            print(f"Пользователь '{user.username}' не имеет прав на редактирование документа '{self.title}'.")

    def save(self, format_type):
        if format_type == "TXT":
            with open(f"{self.title}.txt", "w", encoding="utf-8") as file:
                file.write(self.content)
        elif format_type == "JSON":
            with open(f"{self.title}.json", "w", encoding="utf-8") as file:
                json.dump({"title": self.title, "content": self.content}, file)
        elif format_type == "XML":
            xml_content = dicttoxml.dicttoxml({"title": self.title, "content": self.content})
            with open(f"{self.title}.xml", "wb") as file:
                file.write(xml_content)
        else:
            print("Не поддерживаемый формат.")

    @classmethod
    def load(cls, file_path):
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
                return cls(title=os.path.basename(file_path).replace('.txt', ''), content=content)
        elif file_path.endswith('.json'):
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                return cls(title=data['title'], content=data['content'], doc_type="JSON")
        elif file_path.endswith('.xml'):
            with open(file_path, 'rb') as file:
                data = ET.parse(file).getroot()
                title = data.find('title').text
                content = data.find('content').text
                return cls(title=title, content=content, doc_type="XML")
        else:
            raise ValueError("Unsupported file format")

    def delete(self):
        try:
            os.remove(f"{self.title}.txt")
            os.remove(f"{self.title}.json")
            os.remove(f"{self.title}.xml")
        except FileNotFoundError:
            print(f"Файл(ы) документа '{self.title}' не существуют.")


# Специфические типы документов

class PlainTextDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="PlainText", owner=owner)

class MarkdownDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="Markdown", owner=owner)

class RichTextDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="RichText", owner=owner)


# Реализация Фабрики

class DocumentFactory:
    @staticmethod
    def create_document(doc_type, title, content="", owner=None):
        if doc_type == "PlainText":
            return PlainTextDocument(title, content, owner)
        elif doc_type == "Markdown":
            return MarkdownDocument(title, content, owner)
        elif doc_type == "RichText":
            return RichTextDocument(title, content, owner)
        else:
            raise ValueError(f"Unsupported document type: {doc_type}")


# Класс-менеджер документов

class DocumentManager:
    def __init__(self):
        self.documents = {}

    def create_document(self, title, doc_type="PlainText", owner=None, permissions=None):
        if title in self.documents:
            print("Документ с таким названием уже существует.")
            return None
        doc = DocumentFactory.create_document(doc_type, title, content="", owner=owner)
        if permissions:
            # Обновляем права доступа, заданные администратором
            doc.permissions.update(permissions)
        self.documents[title] = doc
        return doc

    def open_document(self, title):
        return self.documents.get(title)

    def delete_document(self, title):
        if title in self.documents:
            self.documents[title].delete()
            del self.documents[title]
            print(f"Документ '{title}' удалён.")
        else:
            print("Документ не найден.")


