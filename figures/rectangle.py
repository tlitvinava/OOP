# rectangle.py
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.id = None

    def move(self, new_x1, new_y1, new_x2, new_y2):
        self.x1, self.y1, self.x2, self.y2 = new_x1, new_y1, new_x2, new_y2