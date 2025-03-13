class Canvas:
    def __init__(self):
        self.state = []  # Состояние холста, хранит фигуры
        self.next_id = 1  # Следующий доступный ID для фигур

    def draw_figure(self, figure):
        figure.id = self.next_id  # Устанавливаем ID фигуры
        self.state.append(figure)  # Добавляем фигуру в состояние холста
        self.next_id += 1  # Увеличиваем ID для следующей фигуры

    def erase_figure(self, figure_id):
        # Удаляем фигуру по ID
        self.state = [fig for fig in self.state if fig.id != figure_id]

    def get_figure(self, figure_id):
        # Находим и возвращаем фигуру по ID
        for figure in self.state:
            if figure.id == figure_id:
                return figure
        return None  # Если фигура не найдена

    def set_background(self, figure_id, color):
        figure = self.get_figure(figure_id)
        if figure:
            figure.color = color  # Устанавливаем новый цвет фигуры
            print(f"Цвет фигуры с ID {figure_id} изменён на {color}")

    def display(self):
        # Отображаем все фигуры на холсте
        for figure in self.state:
            print(figure)  # Выводим информацию о фигурах