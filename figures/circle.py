from figures.figure import Figure

class Circle(Figure):
    def __init__(self, params):
        super().__init__(params)
        self.x = params['x']
        self.y = params['y']
        self.radius = params['radius']
        self.color = params['color']

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           fill=self.color, outline=self.color)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def erase(self, canvas):
        pass
