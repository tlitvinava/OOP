import json
import os
import dicttoxml
from xml.etree import ElementTree as ET

class Document:
    def __init__(self, title, content="", doc_type="PlainText"):
        self.title = title
        self.content = content
        self.doc_type = doc_type

    def open(self, user):
        if user.can_view():
            self.read_only = not user.can_edit()
            mode = "read-only" if self.read_only else "editable"
            print(f"{user.username} opened '{self.title}' in {mode} mode.")
        else:
            print(f"{user.username} does not have permission to view '{self.title}'.")

    def edit(self, user, new_content):
        if user.can_edit():
            self.content = new_content
            print(f"{user.username} edited '{self.title}'.")
        else:
            print(f"{user.username} does not have permission to edit '{self.title}'.")

    def save(self, format_type):
        if format_type == "TXT":
            with open(f"{self.title}.txt", "w") as file:
                file.write(self.content)
        elif format_type == "JSON":
            with open(f"{self.title}.json", "w") as file:
                json.dump({"title": self.title, "content": self.content}, file)
        elif format_type == "XML":
            xml_content = dicttoxml.dicttoxml({"title": self.title, "content": self.content})
            with open(f"{self.title}.xml", "wb") as file:
                file.write(xml_content)

    @classmethod
    def load(cls, file_path):
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                content = file.read()
                return cls(title=os.path.basename(file_path).replace('.txt', ''), content=content)
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as file:
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
            print(f"File {self.title} does not exist.")

class DocumentManager:
    def __init__(self):
        self.documents = {}

    def create_document(self, title):
        if title in self.documents:
            print("Document already exists.")
            return None
        doc = Document(title)
        self.documents[title] = doc
        return doc

    def open_document(self, title):
        return self.documents.get(title)

    def delete_document(self, title):
        if title in self.documents:
            self.documents[title].delete()
            del self.documents[title]
            print(f"Document '{title}' deleted.")
        else:
            print("Document not found.")

if __name__ == "__main__":
    manager = DocumentManager()
    
    # Создание документа
    doc = manager.create_document("MyDocument")
    
    # Добавление контента и сохранение в разных форматах
    doc.content = "This is a test content."
    doc.save("TXT")
    doc.save("JSON")
    doc.save("XML")

    # Загрузка документа
    loaded_doc = Document.load("MyDocument.json")
    print(loaded_doc.title, loaded_doc.content)

    # Удаление документа
    manager.delete_document("MyDocument")