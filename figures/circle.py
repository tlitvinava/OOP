# circle.py
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.id = None

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y