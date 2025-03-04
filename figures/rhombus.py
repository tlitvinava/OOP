class Rhombus:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, color):
        self.id = None
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.color = color

    def __str__(self):
        return f"Rhombus {self.id} {self.x1} {self.y1} {self.x2} {self.y2} {self.x3} {self.y3} {self.x4} {self.y4} {self.color}"
