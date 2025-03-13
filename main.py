from canvas import Canvas
from command import Command
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.triangle import Triangle

# main.py
from canvas import Canvas
from ansi_colors import ANSI_COLORS  # Импортируем ANSI коды2

# main.py
from canvas import Canvas
from ansi_colors import ANSI_COLORS  # Импортируем ANSI коды

def main():
    canvas = None
    while True:
        print("\nМеню:")
        print('1. Отобразить холст')
        print('2. Нарисовать фигуру')
        print('3. Удалить фигуру')
        print('4. Переместить фигуру')
        print('5. Экспортировать холст в файл')
        print('6. Импортировать холст из файла')
        print('7. Изменить цвет символов')
        print('8. Изменить цвет фона')
        print('9. Undo')  # Новый пункт меню
        print('10. Redo')  # Новый пункт меню

        choice = int(input("Выберите: "))
        if choice == 1:
            if canvas is None:
                print("У вас нету холста. Создайте новый холст:")
                height = int(input("Введите высоту: "))
                width = int(input("Введите ширину: "))
                canvas = Canvas(width, height)

            print("Текущий холст:")
            canvas.display()
        
        elif choice == 2:
            if canvas is None:
                print("У вас нету холста. Создайте новый холст:")
                height = int(input("Введите высоту: "))
                width = int(input("Введите ширину: "))
                canvas = Canvas(width, height)

            print("Какую фигуру вы хотите нарисовать?")
            print("1. Прямоугольник")
            print("2. Круг")
            print("3. Треугольник")
            shape_choice = int(input("Выберите фигуру: "))

            if shape_choice == 1:
                print("Введите координаты прямоугольника:")
                x1 = int(input("x1: "))
                y1 = int(input("y1: "))
                x2 = int(input("x2: "))
                y2 = int(input("y2: "))
                rectangle = Rectangle(x1, y1, x2, y2)
                canvas.draw_figure(rectangle)

            elif shape_choice == 2:
                print("Введите координаты круга:")
                x = int(input("Центр x: "))
                y = int(input("Центр y: "))
                radius = int(input("Радиус: "))
                circle = Circle(x, y, radius)
                canvas.draw_figure(circle)

            elif shape_choice == 3:
                print("Введите координаты треугольника:")
                x1 = int(input("x1: "))
                y1 = int(input("y1: "))
                x2 = int(input("x2: "))
                y2 = int(input("y2: "))
                x3 = int(input("x3: "))
                y3 = int(input("y3: "))
                triangle = Triangle(x1, y1, x2, y2, x3, y3)
                canvas.draw_figure(triangle)

            print("Текущий холст:")
            canvas.display()

        elif choice == 3:
            if canvas is None:
                print("У вас нету холста. Создайте новый холст:")
                height = int(input("Введите высоту: "))
                width = int(input("Введите ширину: "))
                canvas = Canvas(width, height)

            figure_id = int(input("Введите ID фигуры для удаления: "))
            canvas.remove_figure(figure_id)

            print("Текущий холст после удаления фигуры:")
            canvas.display()

        elif choice == 4:
            if canvas is None:
                print("У вас нету холста. Создайте новый холст:")
                height = int(input("Введите высоту: "))
                width = int(input("Введите ширину: "))
                canvas = Canvas(width, height)

            figure_id = int(input("Введите ID фигуры для перемещения: "))
            for figure in canvas.figures:
                if figure.id == figure_id:
                    if isinstance(figure, Rectangle):
                        new_x1 = int(input("Введите новый x1: "))
                        new_y1 = int(input("Введите новый y1: "))
                        new_x2 = int(input("Введите новый x2: "))
                        new_y2 = int(input("Введите новый y2: "))
                        canvas.move_figure(figure_id, (new_x1, new_y1, new_x2, new_y2))
                    elif isinstance(figure, Circle):
                        new_x = int(input("Введите новый центр x: "))
                        new_y = int(input("Введите новый центр y: "))
                        canvas.move_figure(figure_id, (new_x, new_y))
                    elif isinstance(figure, Triangle):
                        new_x1 = int(input("Введите новый x1: "))
                        new_y1 = int(input("Введите новый y1: "))
                        new_x2 = int(input("Введите новый x2: "))
                        new_y2 = int(input("Введите новый y2: "))
                        new_x3 = int(input("Введите новый x3: "))
                        new_y3 = int(input("Введите новый y3: "))
                        canvas.move_figure(figure_id, (new_x1, new_y1, new_x2, new_y2, new_x3, new_y3))
                    break
            else:
                print("Фигура с таким ID не найдена.")

            print("Текущий холст после перемещения фигуры:")
            canvas.display()

        elif choice == 5:
            if canvas is None:
                print("У вас нету холста. Создайте новый холст:")
                height = int(input("Введите высоту: "))
                width = int(input("Введите ширину: "))
                canvas = Canvas(width, height)

            filename = input("Введите имя файла для экспорта (например, canvas.txt): ")
            with open(filename, 'w') as file:
                for row in canvas.state:
                    file.write(''.join(row) + '\n')
            print(f"Холст экспортирован в файл {filename}.")

        elif choice == 6:
            filename = input("Введите имя файла для импорта (например, canvas.txt): ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    if canvas is None:
                        height = len(lines)
                        width = max(len(line.strip()) for line in lines)
                        canvas = Canvas(width, height)

                    for i, line in enumerate(lines):
                        canvas.state[i] = list(line.strip())
                print(f"Холст импортирован из файла {filename}.")
                canvas.display()
            except FileNotFoundError:
                print("Файл не найден. Пожалуйста, проверьте имя файла.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == 7:
            print("Выберите цвет символов:")
            for color in ANSI_COLORS.keys():
                print(color)
            color_choice = input("Введите цвет: ")
            if color_choice in ANSI_COLORS:
                canvas.set_symbol_color(color_choice)
                print(f"Цвет символов изменен на {color_choice}.")
            else:
                print("Неверный выбор цвета.")

        elif choice == 8:
            print("Выберите цвет фона:")
            for color in ANSI_COLORS.keys():
                print(color)
            color_choice = input("Введите цвет: ")
            if color_choice in ANSI_COLORS:
                canvas.set_background_color(color_choice)
                print(f"Цвет фона изменен на {color_choice}.")
            else:
                print("Неверный выбор цвета.")

        elif choice == 9:
            canvas.undo()
            print("Отменено последнее действие.")
            canvas.display()

        elif choice == 10:
            canvas.redo()
            print("Возврат к последнему действию.")
            canvas.display()

if __name__ == '__main__':
    main()