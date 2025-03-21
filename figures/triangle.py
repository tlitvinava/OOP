import math

class Triangle:
    def __init__(self, x1, y1, side_a, side_b, side_c, color="\033[41m"):
        self.x1 = x1
        self.y1 = y1
        self.side_a = side_a  
        self.side_b = side_b 
        self.side_c = side_c  
        self.color = color          
        self.x2 = x1 + side_a
        self.y2 = y1
        
        s = (side_a + side_b + side_c) / 2
        height = (2 / side_a) * math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

        self.x3 = x1
        self.y3 = y1 + height

    def move(self, new_x1, new_y1):
        self.x1, self.y1 = new_x1, new_y1
        self.x2 = new_x1 + self.side_a
        self.y2 = new_y1
        s = (self.side_a + self.side_b + self.side_c) / 2
        height = (2 / self.side_a) * math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        self.x3 = new_x1
        self.y3 = new_y1 + height

    def get_vertices(self):
        return (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)
