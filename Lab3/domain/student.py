class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def validate(self):
        if not self.name:
            raise ValueError("Имя не может быть пустым")
        if self.grade < 0:
            raise ValueError("Оценка не может быть отрицательной")
