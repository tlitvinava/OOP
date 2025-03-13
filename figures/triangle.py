from utils import convert_color_to_ansi

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        self.id = None
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = color

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: x1, y1, x2, y2, x3, y3 (координаты вершин треугольника), color (цвет)"

    def draw_ascii(self):
        min_x = min(self.x1, self.x2, self.x3)
        max_x = max(self.x1, self.x2, self.x3)
        min_y = min(self.y1, self.y2, self.y3)
        max_y = max(self.y1, self.y2, self.y3)

        color_code = convert_color_to_ansi(self.color)
        reset_code = "\033[0m"

        for y in range(max_y + 1):
            for x in range(min_x, max_x + 1):
                if self.is_point_in_triangle(x, y):
                    print(f"{color_code}*{reset_code}", end="")
                else:
                    print(" ", end="")
            print()

    def is_point_in_triangle(self, x, y):
        area = 0.5 * (-self.y2 * self.x3 + self.y1 * (-self.x2 + self.x3) + self.x1 * (self.y2 - self.y3) + self.x2 * self.y3)
        s = 1 / (2 * area) * (self.y1 * self.x3 - self.x1 * self.y3 + (self.y3 - self.y1) * x + (self.x1 - self.x3) * y)
        t = 1 / (2 * area) * (self.x1 * self.y2 - self.y1 * self.x2 + (self.y1 - self.y2) * x + (self.x2 - self.x1) * y)
        return s >= 0 and t >= 0 and (s + t <= 1)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        self.x3 += dx
        self.y3 += dy

    def __str__(self):
        return f"Triangle {self.id} {self.x1} {self.y1} {self.x2} {self.y2} {self.x3} {self.y3} {self.color}"