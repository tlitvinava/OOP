from figures.figure import Figure

class Rectangle(Figure):
    def __init__(self, params):
        super().__init__(params)
        self.x1 = params['x1']
        self.y1 = params['y1']
        self.x2 = params['x2']
        self.y2 = params['y2']
        self.color = params['color']

    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.color)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def erase(self, canvas):
        pass
