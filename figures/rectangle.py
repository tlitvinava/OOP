class Rectangle:
    def __init__(self, x1, y1, x2, y2, color):
        self.id = None
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: x1 (верхний левый угол x), y1 (верхний левый угол y), x2 (правый нижний угол x), y2 (правый нижний угол y), color (цвет)"

    def __str__(self):
        return f"Rectangle {self.id} {self.x1} {self.y1} {self.x2} {self.y2} {self.color}"
