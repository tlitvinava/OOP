class Star:
    def __init__(self, points, color):
        self.id = None
        self.points = points
        self.color = color

    def __str__(self):
        return f"Star {self.id} {self.points} {self.color}"
