import pickle
from tkinter import filedialog

class FileHandler:
    def __init__(self, canvas):
        self.canvas = canvas

    def save(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pkl",
                                                filetypes=[("Pickle files", "*.pkl"),
                                                           ("All files", "*.*")])
        if filename:
            with open(filename, 'wb') as f:
                pickle.dump(self.canvas.state, f)

    def load(self):
        filename = filedialog.askopenfilename(defaultextension=".pkl",
                                              filetypes=[("Pickle files", "*.pkl"),
                                                         ("All files", "*.*")])
        if filename:
            with open(filename, 'rb') as f:
                state = pickle.load(f)
                self.canvas.clear_canvas()
                self.canvas.state = state
                for action, obj in self.canvas.state:
                    if action == 'draw':
                        obj.draw(self.canvas.canvas)
                    elif action == 'background':
                        obj.apply(self.canvas.canvas)
