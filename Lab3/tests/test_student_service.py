# tests/test_student_service.py

import unittest
from application.student_service import StudentService
from domain.dtos import StudentDTO

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.service = StudentService()
        # В реальном проекте здесь можно использовать mock для репозитория и API

    def test_add_student_with_valid_data(self):
        student_dto = StudentDTO("Alice", 85.0)
        quote = self.service.add_student_with_quote(student_dto)
        self.assertIsNotNone(quote)
        self.assertTrue(hasattr(quote, "content"))
        self.assertTrue(hasattr(quote, "author"))

    def test_invalid_student_grade(self):
        student_dto = StudentDTO("Bob", -10)
        with self.assertRaises(ValueError):
            self.service.add_student_with_quote(student_dto)

if __name__ == "__main__":
    unittest.main()
