from canvas import Canvas
from command import Command
from figures.circle import Circle
from figures.hexagon import Hexagon
from figures.line import Line
from figures.rectangle import Rectangle
from figures.rhombus import Rhombus
from figures.square import Square
from figures.star import Star
from figures.triangle import Triangle

def main():
    canvas = Canvas()
    command = Command(canvas)

    while True:
        print("Меню:")
        print("1. Нарисовать фигуру")
        print("2. Удалить фигуру")
        print("3. Отменить действие")
        print("4. Повторить действие")
        print("5. Показать холст")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            figure_type = input("Введите тип фигуры (circle, hexagon, line, rectangle, rhombus, square, star, triangle): ").lower()
            params = list(map(int, input("Введите параметры (через пробел): ").split()))
            color = input("Введите цвет: ")

            if figure_type == "circle":
                figure = Circle(*params, color)
            elif figure_type == "hexagon":
                figure = Hexagon(*params, color)
            elif figure_type == "line":
                figure = Line(*params, color)
            elif figure_type == "rectangle":
                figure = Rectangle(*params, color)
            elif figure_type == "rhombus":
                figure = Rhombus(*params, color)
            elif figure_type == "square":
                figure = Square(*params, color)
            elif figure_type == "star":
                figure = Star(params, color)
            elif figure_type == "triangle":
                figure = Triangle(*params, color)
            else:
                print("Неизвестная фигура. Доступные фигуры: circle, hexagon, line, rectangle, rhombus, square, star, triangle")
                continue

            command.execute(('draw', figure))
            print(f"Нарисована {figure_type} с параметрами {params} и цветом {color}")

        elif choice == '2':
            figure_id = int(input("Введите ID фигуры для удаления: "))
            command.execute(('erase', figure_id))
            print(f"Удалена фигура с ID {figure_id}")

        elif choice == '3':
            command.undo()
            print("Последнее действие отменено")

        elif choice == '4':
            command.redo()
            print("Последнее отмененное действие повторено")

        elif choice == '5':
            canvas.display()

        elif choice == '6':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
