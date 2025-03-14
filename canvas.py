from figures.rectangle import Rectangle
from figures.circle import Circle
from figures.triangle import Triangle
from ansi_colors import ANSI_COLORS  

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = Canvas.init_state(width, height)
        self.figures = []
        self.next_id = 1
        self.symbol_color = ANSI_COLORS["reset"]  # Initial symbol color (reset)
        self.background_color = ANSI_COLORS["reset"]  # Initial background color (reset)
        self.undo_stack = []  # Stack for undo
        self.redo_stack = []  # Stack for redo

    @staticmethod
    def init_state(width, height):
        state = []
        for _ in range(height):
            state.append(list("=" * width))
        return state

    def save_state(self):
        self.undo_stack.append((self.state.copy(), self.figures.copy()))

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append((self.state.copy(), self.figures.copy()))
            self.state, self.figures = self.undo_stack.pop()
            self.update_state()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append((self.state.copy(), self.figures.copy()))
            self.state, self.figures = self.redo_stack.pop()
            self.update_state()

    def draw_figure(self, figure):
        self.save_state()  # Save state before change
        figure.id = self.next_id
        self.figures.append(figure)
        self.update_state()

    def remove_figure(self, figure_id):
        self.save_state()  # Save state before change
        self.figures = [fig for fig in self.figures if fig.id != figure_id]
        self.update_state()

    def move_figure(self, figure_id, new_coordinates):
        self.save_state()  # Save state before change
        for figure in self.figures:
            if figure.id == figure_id:
                figure.move(*new_coordinates)  # Assuming the figure has a move method
                break
        self.update_state()

    def update_state(self):
        self.state = Canvas.init_state(self.width, self.height)
        for figure in self.figures:
            self.draw_figure_to_state(self.state, figure)

    def draw_figure_to_state(self, state, figure):
        if isinstance(figure, Rectangle):
            upper_row = state[figure.y1 - 1]
            for i in range(figure.x1 - 1, figure.x2):
                upper_row[i] = self.symbol_color + '*' + ANSI_COLORS["reset"]
            lower_row = state[figure.y2 - 1]
            for i in range(figure.x1 - 1, figure.x2):
                lower_row[i] = self.symbol_color + '*' + ANSI_COLORS["reset"]
            for i in range(figure.y1 - 1, figure.y2):
                state[i][figure.x1 - 1] = self.symbol_color + '*' + ANSI_COLORS["reset"]
                state[i][figure.x2 - 1] = self.symbol_color + '*' + ANSI_COLORS["reset"]
        
        elif isinstance(figure, Circle):
            for y in range(figure.y - figure.radius, figure.y + figure.radius + 1):
                for x in range(figure.x - figure.radius, figure.x + figure.radius + 1):
                    if (x - figure.x) ** 2 + (y - figure.y) ** 2 <= figure.radius ** 2:
                        if 0 <= x < self.width and 0 <= y < self.height:
                            state[y][x] = self.symbol_color + '*' + ANSI_COLORS["reset"]

        elif isinstance(figure, Triangle):
            self.draw_line(figure.x1, figure.y1, figure.x2, figure.y2, '*', state)
            self.draw_line(figure.x2, figure.y2, figure.x3, figure.y3, '*', state)
            self.draw_line(figure.x3, figure.y3, figure.x1, figure.y1, '*', state)

    def draw_line(self, x1, y1, x2, y2, char, state):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 < self.width and 0 <= y1 < self.height:
                state[y1][x1] = self.symbol_color + char + ANSI_COLORS["reset"]
            if x1 == x2 and y1 == y2:
                break
            err2 = err * 2
            if err2 > -dy:
                err -= dy
                x1 += sx
            if err2 < dx:
                err += dx
                y1 += sy

    def set_background_color(self, color):
        if color in ANSI_COLORS:
            self.background_color = ANSI_COLORS[color]
            self.display()  # Redraw the canvas with the new background color

    def set_symbol_color(self, color):
        if color in ANSI_COLORS:
            self.symbol_color = ANSI_COLORS[color]
            self.display()  # Redraw the canvas with the new symbol color

    def display(self):
        print(self.background_color, end="")  # Set the background color
        for row in self.state:
            print("".join(row))
        print(ANSI_COLORS["reset"], end="")  # Reset color