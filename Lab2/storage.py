# import os
# import json
# import dicttoxml
# import sqlite3
# from abc import ABC, abstractmethod

# # Абстрактный класс стратегии сохранения
# class StorageStrategy(ABC):
#     @abstractmethod
#     def save(self, document, format_type):
#         pass

# # Локальная стратегия. Файлы сохраняются в папке local_storage.
# class LocalStorageStrategy(StorageStrategy):
#     def __init__(self, folder="local_storage"):
#         self.folder = folder
#         if not os.path.exists(self.folder):
#             os.makedirs(self.folder)
    
#     def save(self, document, format_type):
#         if format_type == "TXT":
#             file_path = os.path.join(self.folder, f"{document.title}.txt")
#             with open(file_path, "w", encoding="utf-8") as file:
#                 file.write(document.content)
#         elif format_type == "JSON":
#             file_path = os.path.join(self.folder, f"{document.title}.json")
#             with open(file_path, "w", encoding="utf-8") as file:
#                 json.dump({"title": document.title, "content": document.content}, file, indent=4)
#         elif format_type == "XML":
#             file_path = os.path.join(self.folder, f"{document.title}.xml")
#             xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
#             with open(file_path, "wb") as file:
#                 file.write(xml_content)
#         else:
#             print("Неподдерживаемый формат для локального сохранения.")
#         print(f"Документ '{document.title}' успешно сохранён локально в папке '{self.folder}'.")

# # Симуляция облачного хранилища – файлы сохраняются в папке cloud_storage.
# class CloudStorageStrategy(StorageStrategy):
#     def __init__(self, folder="cloud_storage"):
#         self.folder = folder
#         if not os.path.exists(self.folder):
#             os.makedirs(self.folder)
    
#     def save(self, document, format_type):
#         if format_type == "TXT":
#             file_path = os.path.join(self.folder, f"{document.title}.txt")
#             with open(file_path, "w", encoding="utf-8") as file:
#                 file.write(document.content)
#         elif format_type == "JSON":
#             file_path = os.path.join(self.folder, f"{document.title}.json")
#             with open(file_path, "w", encoding="utf-8") as file:
#                 json.dump({"title": document.title, "content": document.content}, file, indent=4)
#         elif format_type == "XML":
#             file_path = os.path.join(self.folder, f"{document.title}.xml")
#             xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
#             with open(file_path, "wb") as file:
#                 file.write(xml_content)
#         else:
#             print("Неподдерживаемый формат для облачного сохранения.")
#         print(f"Документ '{document.title}' успешно сохранён в облаке (папка '{self.folder}').")

# # Стратегия сохранения в базу данных SQLite
# class SQLiteStorageStrategy(StorageStrategy):
#     def __init__(self, db_path="documents.db"):
#         self.db_path = db_path
#         self._init_db()
    
#     def _init_db(self):
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS documents (
#                 title TEXT PRIMARY KEY,
#                 content TEXT,
#                 doc_type TEXT
#             )
#         ''')
#         conn.commit()
#         conn.close()
    
#     def save(self, document, format_type=None):
#         # Здесь format_type не используется – сохраняем данные в базе как есть.
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         # Если документ с таким названием уже существует, обновляем его
#         cursor.execute('''
#             INSERT INTO documents (title, content, doc_type)
#             VALUES (?, ?, ?)
#             ON CONFLICT(title) DO UPDATE SET
#                 content=excluded.content,
#                 doc_type=excluded.doc_type
#         ''', (document.title, document.content, document.doc_type))
#         conn.commit()
#         conn.close()
#         print(f"Документ '{document.title}' успешно сохранён в базе данных SQLite ('{self.db_path}').")


import os
import json
import pickle
import io
import dicttoxml
from abc import ABC, abstractmethod
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
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
                json.dump({"title": document.title,
                          "content": document.content}, file, indent=4)
        elif format_type == "XML":
            file_path = os.path.join(self.folder, f"{document.title}.xml")
            xml_content = dicttoxml.dicttoxml(
                {"title": document.title, "content": document.content})
            with open(file_path, "wb") as file:
                file.write(xml_content)
        else:
            print("Неподдерживаемый формат для локального сохранения.")
        print(
            f"Документ '{document.title}' успешно сохранён локально в папке '{self.folder}'.")

# Симуляция облачного хранилища – файлы сохраняются в папке cloud_storage.


class CloudStorageStrategy(StorageStrategy):
    def __init__(self, credentials_path="credentials.json", token_path="token.pickle"):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.SCOPES = ['https://www.googleapis.com/auth/drive.file']
        self.service = self.get_drive_service()

    def get_drive_service(self):
        creds = None
        if os.path.exists(self.token_path):
            with open(self.token_path, "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.token_path, "wb") as token:
                pickle.dump(creds, token)
        service = build('drive', 'v3', credentials=creds)
        return service

    def save(self, document, format_type):
        # Подготавливаем данные для различных форматов
        if format_type == "TXT":
            ext = ".txt"
            data = document.content.encode('utf-8')  # переводим строку в байты
            mimetype = "text/plain"
        elif format_type == "JSON":
            ext = ".json"
            data = json.dumps(
                {"title": document.title, "content": document.content}, indent=4).encode('utf-8')
            mimetype = "application/json"
        elif format_type == "XML":
            ext = ".xml"
            data = dicttoxml.dicttoxml(
                {"title": document.title, "content": document.content})
            mimetype = "application/xml"
        else:
            print("Неподдерживаемый формат для сохранения в Google Drive.")
            return

        # Используем BytesIO для хранения данных в памяти
        fh = io.BytesIO(data)

        # Передаём данные через MediaIoBaseUpload
        media = MediaIoBaseUpload(fh, mimetype=mimetype, resumable=False)
        file_metadata = {"name": f"{document.title}{ext}"}
        uploaded_file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

        # Формируем ссылку для просмотра файла
        file_id = uploaded_file.get("id")
        view_link = f"https://drive.google.com/file/d/{file_id}/view"

        print(
            f"Документ '{document.title}' успешно сохранён в Google Drive с id: {file_id}.")
        print(f"Ссылка для просмотра файла: {view_link}")
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
        print(
            f"Документ '{document.title}' успешно сохранён в базе данных SQLite ('{self.db_path}').")