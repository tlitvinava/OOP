class Toolbox:
    def __init__(self, canvas):
        self.canvas = canvas
        self.current_tool = None

    def select_tool(self, tool):
        self.current_tool = tool

    def apply_tool(self, x, y, **kwargs):
        if self.current_tool:
            self.current_tool.use(self.canvas, x, y, **kwargs)

# Базовый класс для инструментов
class Tool:
    def use(self, canvas, x, y, **kwargs):
        raise NotImplementedError("Метод use должен быть реализован в подклассе")

# Инструмент: Кисть (Brush)
class Brush(Tool):
    def use(self, canvas, x, y, **kwargs):
        color = kwargs.get('color', 'black')
        size = kwargs.get('size', 5)
        canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=color)

# Инструмент: Ластик (Eraser)
class Eraser(Tool):
    def use(self, canvas, x, y, **kwargs):
        size = kwargs.get('size', 20)
        canvas.create_oval(x - size, y - size, x + size, y + size, fill='white', outline='white')
