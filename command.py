class Command:
    def __init__(self, canvas):
        self.canvas = canvas
        self.history = []
        self.undo_stack = []

    def execute(self, action):
        action_type, figure = action
        if action_type == 'draw':
            self.canvas.draw_figure(figure)
        elif action_type == 'erase':
            self.canvas.erase_figure(figure)
        self.history.append(action)
        self.canvas.display()

    def undo(self):
        if self.history:
            last_action = self.history.pop()
            self.undo_stack.append(last_action)
            self.canvas.display()

    def redo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.execute(action)
            self.canvas.display()
