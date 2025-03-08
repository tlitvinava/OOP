class Star:
    def __init__(self, points, color):
        self.id = None
        self.points = points
        self.color = color

    @staticmethod
    def get_input_prompt():
        return "Введите параметры: points (координаты вершин звезды через пробел, например: x1 y1 x2 y2 ...), color (цвет)"

    def __str__(self):
        return f"Star {self.id} {self.points} {self.color}"
