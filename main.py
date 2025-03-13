from canvas import Canvas
from command import Command
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.triangle import Triangle

def main():
    # Инициализация холста и командного менеджера
    canvas = Canvas()
    command = Command(canvas)

    # Словарь доступных фигур
    figure_classes = {
        1: Circle,
        2: Rectangle,
        3: Triangle,
    }

    # Основной цикл программы
    while True:
        print("\nМеню:")
        print("1. Нарисовать фигуру")
        print("2. Удалить фигуру")
        print("3. Переместить фигуру")
        print("4. Установить фон фигуры")
        print("5. Сохранить холст в файл")
        print("6. Загрузить холст из файла")
        print("7. Отменить действие")
        print("8. Повторить действие")
        print("9. Показать холст")
        print("10. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':  # Нарисовать фигуру
            print("\nДоступные фигуры:")
            for num, figure_class in figure_classes.items():
                print(f"{num}. {figure_class.__name__}")

            try:
                figure_choice = int(input("Введите номер фигуры для рисования: "))
                figure_class = figure_classes.get(figure_choice)
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
            except ValueError:
                print("Ошибка: Введите номер фигуры.")

        elif choice == '2':  # Удалить фигуру
            try:
                figure_id = int(input("Введите ID фигуры для удаления: "))
                command.execute(('erase', figure_id))
                print(f"Удалена фигура с ID {figure_id}")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == '3':  # Переместить фигуру
            try:
                figure_id = int(input("Введите ID фигуры для перемещения: "))
                new_x = int(input("Введите новое значение X: "))
                new_y = int(input("Введите новое значение Y: "))
                command.execute(('move', figure_id, new_x, new_y))
                print(f"Перемещена фигура с ID {figure_id} на ({new_x}, {new_y})")
            except ValueError:
                print("Ошибка: Введите корректные значения.")

        elif choice == '4':  # Установить фон фигуры
            try:
                figure_id = int(input("Введите ID фигуры для установки фона: "))
                background_color = input("Введите цвет фона: ")
                command.execute(('set_background', figure_id, background_color))
                print(f"Установлен фон для фигуры с ID {figure_id} цветом {background_color}")
                # Делаем обновление холста
                canvas.display()
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == '5':  # Сохранить холст в файл
            filename = input("Введите имя файла для сохранения: ")
            command.save_canvas(filename)
            print(f"Холст сохранен в файл {filename}")

        elif choice == '6':  # Загрузить холст из файла
            filename = input("Введите имя файла для загрузки: ")
            command.load_canvas(filename)
            print(f"Холст загружен из файла {filename}")

        elif choice == '7':  # Отменить действие
            command.undo()
            print("Последнее действие отменено")

        elif choice == '8':  # Повторить действие
            command.redo()
            print("Последнее отмененное действие повторено")

        elif choice == '9':  # Показать холст
            print("\nТекущий холст:")
            canvas.display()

        elif choice == '10':  # Выход
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()