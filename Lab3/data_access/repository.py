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

    def add_student(self, student: Student):
        students = self.get_all_students()
        students.append({"name": student.name, "grade": student.grade})
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)

    def get_all_students(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)
