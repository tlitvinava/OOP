class Line:
    def __init__(self, x1, y1, x2, y2, color):
        self.id = None
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def __str__(self):
        return f"Line {self.id} {self.x1} {self.y1} {self.x2} {self.y2} {self.color}"
