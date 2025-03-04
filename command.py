class Command:
    def __init__(self, canvas):
        self.canvas = canvas
        self.history = []

    def execute(self, action):
        # добавить логику выполнения действия
        pass

    def undo(self):
        # логика отката действия
        pass

    def redo(self):
        # логика повторного выполнения действия
        pass
