from utils import convert_color_to_ansi

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

    def draw_ascii(self):
        width = self.x2 - self.x1
        height = self.y2 - self.y1
        
        # Получить ANSI-код цвета
        color_code = convert_color_to_ansi(self.color)
        reset_code = "\033[0m"

        for y in range(self.y1, self.y2):
            for x in range(self.x1, self.x2):
                print(f"{color_code}*{reset_code}", end="")
            print()  # Переход на новую строку

    def __str__(self):
        return f"Rectangle {self.id} {self.x1} {self.y1} {self.x2} {self.y2} {self.color}"
