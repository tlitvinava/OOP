import os
import json
import dicttoxml
import sqlite3
from abc import ABC, abstractmethod

# Абстрактный класс стратегии сохранения
class StorageStrategy(ABC):
    @abstractmethod
    def save(self, document, format_type):
        pass

# Локальная стратегия. Файлы сохраняются в папке local_storage.
class LocalStorageStrategy(StorageStrategy):
    def __init__(self, folder="local_storage"):
        self.folder = folder
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
    
    def save(self, document, format_type):
        if format_type == "TXT":
            file_path = os.path.join(self.folder, f"{document.title}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(document.content)
        elif format_type == "JSON":
            file_path = os.path.join(self.folder, f"{document.title}.json")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump({"title": document.title, "content": document.content}, file, indent=4)
        elif format_type == "XML":
            file_path = os.path.join(self.folder, f"{document.title}.xml")
            xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
            with open(file_path, "wb") as file:
                file.write(xml_content)
        else:
            print("Неподдерживаемый формат для локального сохранения.")
        print(f"Документ '{document.title}' успешно сохранён локально в папке '{self.folder}'.")

# Симуляция облачного хранилища – файлы сохраняются в папке cloud_storage.
class CloudStorageStrategy(StorageStrategy):
    def __init__(self, folder="cloud_storage"):
        self.folder = folder
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
    
    def save(self, document, format_type):
        if format_type == "TXT":
            file_path = os.path.join(self.folder, f"{document.title}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(document.content)
        elif format_type == "JSON":
            file_path = os.path.join(self.folder, f"{document.title}.json")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump({"title": document.title, "content": document.content}, file, indent=4)
        elif format_type == "XML":
            file_path = os.path.join(self.folder, f"{document.title}.xml")
            xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
            with open(file_path, "wb") as file:
                file.write(xml_content)
        else:
            print("Неподдерживаемый формат для облачного сохранения.")
        print(f"Документ '{document.title}' успешно сохранён в облаке (папка '{self.folder}').")

# Стратегия сохранения в базу данных SQLite
class SQLiteStorageStrategy(StorageStrategy):
    def __init__(self, db_path="documents.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                title TEXT PRIMARY KEY,
                content TEXT,
                doc_type TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def save(self, document, format_type=None):
        # Здесь format_type не используется – сохраняем данные в базе как есть.
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Если документ с таким названием уже существует, обновляем его
        cursor.execute('''
            INSERT INTO documents (title, content, doc_type)
            VALUES (?, ?, ?)
            ON CONFLICT(title) DO UPDATE SET
                content=excluded.content,
                doc_type=excluded.doc_type
        ''', (document.title, document.content, document.doc_type))
        conn.commit()
        conn.close()
        print(f"Документ '{document.title}' успешно сохранён в базе данных SQLite ('{self.db_path}').")
