import tkinter as tk
from canvas import Canvas
from toolbox import Toolbox
from file_handler import FileHandler
from command import Command

class MainApp:
    def __init__(self, root):
        self.canvas = Canvas(root)
        self.toolbox = Toolbox(self.canvas)
        self.file_handler = FileHandler(self.canvas)
        self.command = Command(self.canvas)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
