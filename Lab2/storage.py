# storage.py

import os
import json
import dicttoxml

class StorageStrategy:
    def save(self, document, format_type):
        """Метод для сохранения документа в выбранном формате."""
        raise NotImplementedError("Метод save должен быть реализован.")

    def load(self, file_path):
        """Метод для загрузки документа из хранилища."""
        raise NotImplementedError("Метод load должен быть реализован.")

class LocalStorageStrategy(StorageStrategy):
    def save(self, document, format_type):
        if format_type == "TXT":
            filename = f"{document.title}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(document.content)
        elif format_type == "JSON":
            filename = f"{document.title}.json"
            with open(filename, "w", encoding="utf-8") as file:
                json.dump({"title": document.title, "content": document.content}, file)
        elif format_type == "XML":
            filename = f"{document.title}.xml"
            xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
            with open(filename, "wb") as file:
                file.write(xml_content)
        else:
            print("Не поддерживаемый формат для локального хранилища.")
            return
        print(f"Документ '{document.title}' сохранен локально в формате {format_type}.")

    def load(self, file_path):
        # Реализация метода загрузки аналогична Document.load
        pass

class CloudStorageStrategy(StorageStrategy):
    cloud_dir = "cloud_storage"
    
    def __init__(self):
        if not os.path.exists(self.cloud_dir):
            os.makedirs(self.cloud_dir)

    def _get_path(self, document, format_type):
        ext = ""
        if format_type == "TXT":
            ext = ".txt"
        elif format_type == "JSON":
            ext = ".json"
        elif format_type == "XML":
            ext = ".xml"
        else:
            raise ValueError("Не поддерживаемый формат для облачного хранилища.")
        return os.path.join(self.cloud_dir, document.title + ext)

    def save(self, document, format_type):
        path = self._get_path(document, format_type)
        if format_type == "TXT":
            with open(path, "w", encoding="utf-8") as file:
                file.write(document.content)
        elif format_type == "JSON":
            with open(path, "w", encoding="utf-8") as file:
                json.dump({"title": document.title, "content": document.content}, file)
        elif format_type == "XML":
            xml_content = dicttoxml.dicttoxml({"title": document.title, "content": document.content})
            with open(path, "wb") as file:
                file.write(xml_content)
        print(f"Документ '{document.title}' сохранен в облаке в формате {format_type} по пути: {path}.")

    def load(self, file_path):
        # Реализация метода загрузки аналогична LocalStorageStrategy
        pass
