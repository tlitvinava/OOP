from utils import convert_color_to_ansi

class Circle:
    def __init__(self, x, y, radius, color="red"):
        self.id = None
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: x (координата центра), y (координата центра), radius (радиус), color (цвет)"

    def draw_ascii(self):
        size = self.radius * 2 + 1
        center_x, center_y = self.radius, self.radius

        color_code = convert_color_to_ansi(self.color)
        reset_code = "\033[0m"

        for i in range(size):
            for j in range(size):
                dist = ((i - center_x) ** 2 + (j - center_y) ** 2) ** 0.5
                if dist <= self.radius:
                    print(f"{color_code}*{reset_code}", end="")
                else:
                    print(" ", end="")
            print()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Circle {self.id} {self.x} {self.y} {self.radius} {self.color}"