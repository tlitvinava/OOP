import math

# class Triangle:
#     def __init__(self, x1, y1, base, height, color='reset'):
#         self.x1 = x1  # Вершина в правом углу (прямой угол)
#         self.y1 = y1
#         self.base = base
#         self.height = height
#         self.color = color  # Новый атрибут для хранения цвета
        
#         self.x2 = x1 + base  # Вершина по оси x
#         self.y2 = y1  # Остаётся на одной высоте
#         self.x3 = x1  # Вершина по оси y
#         self.y3 = y1 + height  # Поднимается по оси y

#     def move(self, new_x1, new_y1):
#         # Обновляем координаты вершины в правом углу
#         self.x1, self.y1 = new_x1, new_y1
#         self.x2 = new_x1 + self.base
#         self.y2 = new_y1
#         self.x3 = new_x1
#         self.y3 = new_y1 + self.height

#     def get_vertices(self):
#         return (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)

# class Triangle:
#     def __init__(self, x1, y1, base, height, color=ANSI_COLORS["reset"]):
#         self.x1 = x1
#         self.y1 = y1
#         self.base = base
#         self.height = height
#         self.color = color  # Новый атрибут для хранения цвета

#         self.x2 = x1 + base
#         self.y2 = y1
#         self.x3 = x1
#         self.y3 = y1 + height

#     def move(self, new_x1, new_y1):
#         self.x1, self.y1 = new_x1, new_y1
#         self.x2 = new_x1 + self.base
#         self.y2 = new_y1
#         self.x3 = new_x1
#         self.y3 = new_y1 + self.height

#     def get_vertices(self):
#         return (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)

class Triangle:
    def __init__(self, x1, y1, base, height, color="\033[41m"):
        self.x1 = x1
        self.y1 = y1
        self.base = base
        self.height = height
        self.color = color  # Новый атрибут для хранения цвета

        self.x2 = x1 + base
        self.y2 = y1
        self.x3 = x1
        self.y3 = y1 + height

    def move(self, new_x1, new_y1):
        self.x1, self.y1 = new_x1, new_y1
        self.x2 = new_x1 + self.base
        self.y2 = new_y1
        self.x3 = new_x1
        self.y3 = new_y1 + self.height

    def get_vertices(self):
        return (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)