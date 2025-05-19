# application/student_service.py

from domain.factories import Factory
from data_access.repository import StudentRepository
from integration.quote_api_adapter import QuoteApiAdapter
from domain.dtos import StudentDTO

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()
        self.quote_adapter = QuoteApiAdapter()

    def add_student_with_quote(self, student_dto: StudentDTO):
        # Создаем и валидируем студента
        student = Factory.create_student(student_dto)
        self.repository.add_student(student)
        # Получаем цитату после добавления студента
        quote = self.quote_adapter.fetch_quote()
        return quote

    def get_all_students(self):
        return self.repository.get_all_students()

# integration/quote_api_adapter.py

