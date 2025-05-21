# application/student_service.py

import sys
import os

# Добавляем путь к родительской директории (my_project/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.factories import Factory
from data_access.repository import StudentRepository
from integration.quote_api_adapter import QuoteApiAdapter
from domain.dtos import StudentDTO

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()
        self.quote_adapter = QuoteApiAdapter()

    def add_student_with_quote(self, student_dto: StudentDTO):
        # Создаем объект студента из DTO, выполняется валидация
        student = Factory.create_student(student_dto)
        # Получаем цитату через адаптер
        quote = self.quote_adapter.fetch_quote()
        # Добавляем студента вместе с цитатой в репозиторий
        self.repository.add_student(student, quote)
        return quote

    def get_all_students(self):
        return self.repository.get_all_students()
