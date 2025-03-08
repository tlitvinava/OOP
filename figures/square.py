class Square:
    def __init__(self, x, y, size, color):
        self.id = None
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: x (верхний левый угол), y (верхний левый угол), size (размер стороны), color (цвет)"

    def __str__(self):
        return f"Square {self.id} {self.x} {self.y} {self.size} {self.color}"
