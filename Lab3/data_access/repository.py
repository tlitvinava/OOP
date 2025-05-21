# data_access/repository.py

import json
import os
from domain.student import Student

class StudentRepository:
    def __init__(self, filepath="students.json"):
        self.filepath = filepath
        # Если файла не существует, создаем его с пустым списком
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_student(self, student: Student, quote=None):
        """Добавляет студента вместе с цитатой (если передана) в JSON хранилище."""
        students = self.get_all_students()
        record = {"name": student.name, "grade": student.grade}
        if quote:
            record["quote"] = {"content": quote.content, "author": quote.author}
        students.append(record)
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)

    def get_all_students(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)
