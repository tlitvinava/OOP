from utils import convert_color_to_ansi

class Hexagon:
    def __init__(self, x, y, size, color="red"):
        self.id = None  # Уникальный идентификатор
        self.x = x  # Координата центра по X
        self.y = y  # Координата центра по Y
        self.size = size  # Размер шестиугольника (например, длина стороны)
        self.color = color  # Цвет шестиугольника

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: x (координата центра), y (координата центра), size (размер), color (цвет: red, green, blue, и т.д.)"

    def draw_ascii(self):
        """
        Символическая отрисовка шестиугольника с использованием ASCII и цвета.
        """
        # Размер области для отрисовки
        height = self.size * 2
        width = self.size * 4
        color_code = convert_color_to_ansi(self.color)
        reset_code = "\033 