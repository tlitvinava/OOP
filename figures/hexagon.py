class Hexagon:
    def __init__(self, x, y, size, color):
        self.id = None
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def __str__(self):
        return f"Hexagon {self.id} {self.x} {self.y} {self.size} {self.color}"
