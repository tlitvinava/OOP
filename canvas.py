import tkinter as tk

class Canvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.state = []

    def draw_figure(self, figure):
        # добавить логику рисования фигур
        pass

    def set_background(self, background):
        # добавить логику установки фона
        pass

    def undo(self):
        # добавить логику undo
        pass

    def redo(self):
        # добавить логику redo
        pass
