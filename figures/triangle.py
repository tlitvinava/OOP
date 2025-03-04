from figures.figure import Figure

class Triangle(Figure):
    def __init__(self, params):
        super().__init__(params)
        self.points = params['points']
        self.color = params['color']

    def draw(self, canvas):
        canvas.create_polygon(self.points, fill=self.color, outline=self.color)

    def move(self, dx, dy):
        self.points = [(x+dx, y+dy) for x, y in self.points]

    def erase(self, canvas):
        pass
