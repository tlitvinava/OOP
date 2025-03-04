class Canvas:
    def __init__(self):
        self.state = []
        self.next_id = 1

    def draw_figure(self, figure):
        figure.id = self.next_id
        self.state.append(figure)
        self.next_id += 1

    def erase_figure(self, figure_id):
        self.state = [fig for fig in self.state if fig.id != figure_id]

    def display(self):
        for figure in self.state:
            print(figure)
