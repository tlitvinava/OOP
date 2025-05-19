# data_access/repository.py

import json
import os
from domain.student import Student
import requests
from domain.factories import Factory

class StudentRepository:
    def __init__(self, filepath="students.json"):
        self.filepath = filepath
        # Если файла не существует, создаем его с пустым списком
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_student(self, student: Student):
        students = self.get_all_students()
        students.append({"name": student.name, "grade": student.grade})
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)

    def get_all_students(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)
        

class QuoteApiAdapter:
    def __init__(self, api_url="https://api.quotable.io/random"):
        self.api_url = api_url

    def fetch_quote(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            # Создаем объект QuoteDTO с помощью фабричного метода
            quote = Factory.create_quote(data["content"], data["author"])
            return quote
        else:
            raise Exception("Ошибка при получении цитаты")
