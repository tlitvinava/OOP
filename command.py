from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.triangle import Triangle

class Command:
    def __init__(self, canvas):
        self.canvas = canvas
        self.history = []
        self.undo_stack = []

    def execute(self, action):
        action_type = action[0]

        if action_type == 'draw':
            figure = action[1]
            self.canvas.draw_figure(figure)
            self.history.append(action)
        
        elif action_type == 'erase':
            figure_id = action[1]
            figure = self.canvas.get_figure(figure_id)  # Получаем фигуру по ID
            self.canvas.erase_figure(figure_id)
            self.history.append(('erase', figure))

        elif action_type == 'move':
            figure_id, new_x, new_y = action[1], action[2], action[3]
            figure = self.canvas.get_figure(figure_id)
            if figure:
                old_position = (figure.x, figure.y) if isinstance(figure, Circle) else (figure.x1, figure.y1)
                figure.move(new_x - (figure.x if isinstance(figure, Circle) else figure.x1),
                            new_y - (figure.y if isinstance(figure, Circle) else figure.y1))
                self.history.append(('move', figure_id, old_position, (new_x, new_y)))

                # Отрисовка перемещённой фигуры
                print(f"Перемещена фигура с ID {figure.id} на ({new_x}, {new_y}):")
                figure.draw_ascii()  # Отрисовка фигуры в консоли

        elif action_type == 'set_background':
            figure_id, color = action[1], action[2]
            figure = self.canvas.get_figure(figure_id)
            if figure:
                self.canvas.set_background(figure_id, color)  # Передаем задачу на холст
                self.history.append(('set_background', figure_id, color))

        self.canvas.display()

    def undo(self):
        if self.history:
            last_action = self.history.pop()
            self.undo_stack.append(last_action)

            action_type = last_action[0]
            if action_type == 'draw':
                figure = last_action[1]
                self.canvas.erase_figure(figure.id)  # Удаляем фигуру

            elif action_type == 'erase':
                figure = last_action[1]
                self.canvas.draw_figure(figure)  # Восстанавливаем фигуру

            elif action_type == 'move':
                figure_id, old_position, new_position = last_action[1], last_action[2], last_action[3]
                figure = self.canvas.get_figure(figure_id)
                if figure:
                    if isinstance(figure, Circle):
                        figure.move(old_position[0] - figure.x, old_position[1] - figure.y)  # Вернуть круг на старые координаты
                    else:
                        figure.move(old_position[0] - figure.x1, old_position[1] - figure.y1)  # Вернуть фигуру на старые координаты

            elif action_type == 'set_background':
                figure_id, color = last_action[1], last_action[2]
                figure = self.canvas.get_figure(figure_id)
                if figure:
                    # Вернуть старый цвет фона
                    self.canvas.set_background(figure_id, None)

            self.canvas.display()

    def redo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.execute(action)
            self.canvas.display()

    def save_canvas(self, filename):
        with open(filename, 'w') as f:
            for figure in self.canvas.state:  # Используем self.canvas.state для получения фигур
                f.write(f"{figure.__class__.__name__} {figure}\n")  # Сохраните информацию о фигуре

    def load_canvas(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                figure_type = parts[0]
                params = list(map(str, parts[1:]))  # Параметры могут быть разными типами
                # Создайте фигуру по типу и параметрам
                if figure_type == "Circle":
                    figure = Circle(*map(float, params))  # Предположим, что это Circle
                elif figure_type == "Rectangle":
                    figure = Rectangle(*map(float, params))  # Предположим, что это Rectangle
                elif figure_type == "Triangle":
                    figure = Triangle(*map(float, params))  # Предположим, что это Triangle
                self.canvas.draw_figure(figure)  # Добавьте фигуру на холст