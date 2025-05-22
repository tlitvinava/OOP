from domain.student import Student
from domain.dtos import StudentDTO, QuoteDTO

class Factory:
    @staticmethod
    def create_student(student_dto: StudentDTO) -> Student:
        student = Student(student_dto.name, student_dto.grade)
        student.validate()
        return student

    @staticmethod
    def create_quote(content: str, author: str) -> QuoteDTO:
        return QuoteDTO(content, author)
