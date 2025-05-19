import json
import os
import dicttoxml
from xml.etree import ElementTree as ET
from settings import HistoryManager

class Document:
    def __init__(self, title, content="", doc_type="PlainText", owner=None):
        self.title = title
        self.content = content
        self.doc_type = doc_type
        self.owner = owner  
        self.is_open = True  

    def open(self, user):
        print(f"Документ '{self.title}' открыт.")

    def edit(self, user, new_content):
        self.content = new_content
        print(f"Пользователь '{user.username}' отредактировал документ '{self.title}'.")
        HistoryManager().add_entry(self.title, user.username, "отредактирован")
        if self.owner and user.username != self.owner.username:
            notification = f"Ваш документ '{self.title}' изменён пользователем '{user.username}'."
            if hasattr(self.owner, "notifications"):
                self.owner.notifications.append(notification)

    def save(self, format_type):
        if format_type == "TXT":
            with open(f"{self.title}.txt", "w", encoding="utf-8") as file:
                file.write(self.content)
        elif format_type == "JSON":
            with open(f"{self.title}.json", "w", encoding="utf-8") as file:
                json.dump({"title": self.title, "content": self.content}, file, indent=4)
        elif format_type == "XML":
            xml_content = dicttoxml.dicttoxml({"title": self.title, "content": self.content})
            with open(f"{self.title}.xml", "wb") as file:
                file.write(xml_content)
        else:
            print("Неподдерживаемый формат.")

    @classmethod
    def load(cls, file_path):
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
                doc = cls(title=os.path.basename(file_path).replace('.txt', ''), content=content)
                doc.is_open = True
                return doc
        elif file_path.endswith('.json'):
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                doc = cls(title=data['title'], content=data['content'], doc_type="JSON")
                doc.is_open = True
                return doc
        elif file_path.endswith('.xml'):
            with open(file_path, 'rb') as file:
                root = ET.parse(file).getroot()
                title_element = root.find('title')
                content_element = root.find('content')
                title = title_element.text if title_element is not None and title_element.text is not None else ""
                content = content_element.text if content_element is not None and content_element.text is not None else ""
                doc = cls(title=title, content=content, doc_type="XML")
                doc.is_open = True
                return doc
        else:
            raise ValueError("Неподдерживаемый формат")


class PlainTextDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="PlainText", owner=owner)

class MarkdownDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="Markdown", owner=owner)

class RichTextDocument(Document):
    def __init__(self, title, content="", owner=None):
        super().__init__(title, content, doc_type="RichText", owner=owner)

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

class DocumentManager:
    def __init__(self):
        self.documents = {}

    def create_document(self, title, doc_type="PlainText", owner=None, permissions=None):
        if title in self.documents:
            print("Документ с таким названием уже существует.")
            return None
        doc = DocumentFactory.create_document(doc_type, title, content="", owner=owner)
        if permissions:
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


