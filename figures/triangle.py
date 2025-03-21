# # # triangle.py
# # class Triangle:
# #     def __init__(self, x1, y1, x2, y2, x3, y3):
# #         self.x1, self.y1 = x1, y1
# #         self.x2, self.y2 = x2, y2
# #         self.x3, self.y3 = x3, y3
# #         self.id = None

# #     def move(self, new_x1, new_y1, new_x2, new_y2, new_x3, new_y3):
# #         self.x1, self.y1 = new_x1, new_y1
# #         self.x2, self.y2 = new_x2, new_y2
# #         self.x3, self.y3 = new_x3, new_y3

# import math
# class Triangle:
#     def __init__(self, center_x, center_y, a, b, c):
#         self.cx = center_x
#         self.cy = center_y
#         self.a = a
#         self.b = b
#         self.c = c
        
#         self.x1, self.y1 = self.calculate_vertex_a()
#         self.x2, self.y2 = self.calculate_vertex_b()
#         self.x3, self.y3 = self.calculate_vertex_c()

#     def calculate_vertex_a(self):
#         return (self.cx, self.cy - self.a / 2)

#     def calculate_vertex_b(self):
#         angle_a = math.acos((self.b**2 + self.a**2 - self.c**2) / (2 * self.b * self.a))
#         x_b = self.cx + self.b * math.cos(angle_a)
#         y_b = self.cy + self.b * math.sin(angle_a)
#         return (x_b, y_b)

#     def calculate_vertex_c(self):
#         angle_b = math.acos((self.c**2 + self.a**2 - self.b**2) / (2 * self.c * self.a))
#         x_c = self.cx + self.c * math.cos(math.pi - angle_b)
#         y_c = self.cy + self.c * math.sin(math.pi - angle_b)
#         return (x_c, y_c)


import math

class Triangle:
    def __init__(self, x1, y1, base, height):
        self.x1 = x1  # Вершина в правом углу (прямой угол)
        self.y1 = y1
        self.base = base
        self.height = height
        
        self.x2 = x1 + base  # Вершина по оси x
        self.y2 = y1  # Остаётся на одной высоте
        self.x3 = x1  # Вершина по оси y
        self.y3 = y1 + height  # Поднимается по оси y

    def move(self, new_x1, new_y1):
        # Обновляем координаты вершины в правом углу
        self.x1, self.y1 = new_x1, new_y1
        self.x2 = new_x1 + self.base
        self.y2 = new_y1
        self.x3 = new_x1
        self.y3 = new_y1 + self.height

    def get_vertices(self):
        return (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)