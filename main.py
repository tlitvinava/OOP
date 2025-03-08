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
    # Инициализация холста и командного менеджера
    canvas = Canvas()
    command = Command(canvas)

    # Словарь доступных фигур
    figure_classes = {
        "circle": Circle,
        "hexagon": Hexagon,
        "line": Line,
        "rectangle": Rectangle,
        "rhombus": Rhombus,
        "square": Square,
        "star": Star,
        "triangle": Triangle,
    }

    # Основной цикл программы
    while True:
        print("\nМеню:")
        print("1. Нарисовать фигуру")
        print("2. Удалить фигуру")
        print("3. Отменить действие")
        print("4. Повторить действие")
        print("5. Показать холст")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':  # Нарисовать фигуру
            figure_type = input("Введите тип фигуры (circle, hexagon, line, rectangle, rhombus, square, star, triangle): ").lower()
            figure_class = figure_classes.get(figure_type)
            if not figure_class:
                print("Неизвестная фигура. Попробуйте снова.")
                continue

            print(figure_class.get_input_prompt())  # Печатаем инструкцию для параметров
            params = input("Введите параметры (через пробел): ").split()
            try:
                # Конвертируем параметры в числа (кроме цвета) и создаем фигуру
                figure = figure_class(*map(int, params[:-1]), params[-1])
                command.execute(('draw', figure))  # Выполняем команду рисования
                print(f"\nНарисована фигура: {figure}")
                print("Отрисовка ASCII:")
                figure.draw_ascii()
            except (ValueError, TypeError):
                print("Ошибка ввода параметров. Попробуйте снова.")

        elif choice == '2':  # Удалить фигуру
            try:
                figure_id = int(input("Введите ID фигуры для удаления: "))
                command.execute(('erase', figure_id))
                print(f"Удалена фигура с ID {figure_id}")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == '3':  # Отменить действие
            command.undo()
            print("Последнее действие отменено")

        elif choice == '4':  # Повторить действие
            command.redo()
            print("Последнее отмененное действие повторено")

        elif choice == '5':  # Показать холст
            print("\nТекущий холст:")
            canvas.display()

        elif choice == '6':  # Выход
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
