# # circle.py
# class Circle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.id = None

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

class Circle:
    def __init__(self, x, y, radius, color='\033[41m'):  # По умолчанию цвет сбрасывается
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color  # Новый атрибут для хранения цвета
        self.id = None

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y