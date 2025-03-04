class Circle:
    def __init__(self, x, y, radius, color):
        self.id = None
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Circle {self.id} {self.x} {self.y} {self.radius} {self.color}"
