from canvas import Canvas
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.triangle import Triangle
from ansi_colors import ANSI_COLORS  


def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    canvas = None
    while True:
        print("\nMenu:")
        print('1. Display Canvas')
        print('2. Draw Shape')
        print('3. Remove Shape')
        print('4. Move Shape')
        print('5. Export Canvas to File')
        print('6. Import Canvas from File')
        print('7. Change Symbol Color')
        print('8. Change Background Color')
        print('9. Undo')  # New menu option
        print('10. Redo')  # New menu option
        choice = get_int_input("Choose an option (1-10): ", 1, 10)

        if choice == 1:
            if canvas is None:
                print("You do not have a canvas. Create a new canvas:")
                height = get_int_input("Enter height: ", 1)
                width = get_int_input("Enter width: ", 1)
                canvas = Canvas(width, height)

            print("Current canvas:")
            canvas.display()
        
        elif choice == 2:
            if canvas is None:
                print("You do not have a canvas. Create a new canvas:")
                height = get_int_input("Enter height: ", 1)
                width = get_int_input("Enter width: ", 1)
                canvas = Canvas(width, height)

            print("Which shape would you like to draw?")
            print("1. Rectangle")
            print("2. Circle")
            print("3. Triangle")
            shape_choice = get_int_input("Choose a shape (1-3): ", 1, 3)

            if shape_choice == 1:
                print("Enter the coordinates of the rectangle:")
                x1 = get_int_input("x1: ", 1, canvas.width)
                y1 = get_int_input("y1: ", 1, canvas.height)
                x2 = get_int_input("x2: ", 1, canvas.width)
                y2 = get_int_input("y2: ", 1, canvas.height)
                rectangle = Rectangle(x1, y1, x2, y2)
                canvas.draw_figure(rectangle)

            elif shape_choice == 2:
                print("Enter the coordinates of the circle:")
                x = get_int_input("Center x: ", 1, canvas.width)
                y = get_int_input("Center y: ", 1, canvas.height)
                radius = get_int_input("Radius: ", 1, min(canvas.width, canvas.height) // 2)
                circle = Circle(x, y, radius)
                canvas.draw_figure(circle)

            elif shape_choice == 3:
                print("Enter the coordinates of the triangle:")
                x1 = get_int_input("x1: ", 1, canvas.width)
                y1 = get_int_input("y1: ", 1, canvas.height)
                x2 = get_int_input("x2: ", 1, canvas.width)
                y2 = get_int_input("y2: ", 1, canvas.height)
                x3 = get_int_input("x3: ", 1, canvas.width)
                y3 = get_int_input("y3: ", 1, canvas.height)
                triangle = Triangle(x1, y1, x2, y2, x3, y3)
                canvas.draw_figure(triangle)

            print("Current canvas:")
            canvas.display()

        elif choice == 3:
            if canvas is None:
                print("You do not have a canvas. Create a new canvas:")
                height = get_int_input("Enter height: ", 1)
                width = get_int_input("Enter width: ", 1)
                canvas = Canvas(width, height)

            figure_id = get_int_input("Enter the ID of the shape to remove: ", 1)
            canvas.remove_figure(figure_id)

            print("Current canvas after removing the shape:")
            canvas.display()

        elif choice == 4:
            if canvas is None:
                print("You do not have a canvas. Create a new canvas:")
                height = get_int_input("Enter height: ", 1)
                width = get_int_input("Enter width: ", 1)
                canvas = Canvas(width, height)

            figure_id = get_int_input("Enter the ID of the shape to move: ", 1)
            for figure in canvas.figures:
                if figure.id == figure_id:
                    if isinstance(figure, Rectangle):
                        new_x1 = get_int_input("Enter new x1: ", 1, canvas.width)
                        new_y1 = get_int_input("Enter new y1: ", 1, canvas.height)
                        new_x2 = get_int_input("Enter new x2: ", 1, canvas.width)
                        new_y2 = get_int_input("Enter new y2: ", 1, canvas.height)
                        canvas.move_figure(figure_id, (new_x1, new_y1, new_x2, new_y2))
                    elif isinstance(figure, Circle):
                        new_x = get_int_input("Enter new center x: ", 1, canvas.width)
                        new_y = get_int_input("Enter new center y: ", 1, canvas.height)
                        canvas.move_figure(figure_id, (new_x, new_y))
                    elif isinstance(figure, Triangle):
                        new_x1 = get_int_input("Enter new x1: ", 1, canvas.width)
                        new_y1 = get_int_input("Enter new y1: ", 1, canvas.height)
                        new_x2 = get_int_input("Enter new x2: ", 1, canvas.width)
                        new_y2 = get_int_input("Enter new y2: ", 1, canvas.height)
                        new_x3 = get_int_input("Enter new x3: ", 1, canvas.width)
                        new_y3 = get_int_input("Enter new y3: ", 1, canvas.height)
                        canvas.move_figure(figure_id, (new_x1, new_y1, new_x2, new_y2, new_x3, new_y3))
                    break
            else:
                print("No shape found with that ID.")

            print("Current canvas after moving the shape:")
            canvas.display()

        elif choice == 5:
            if canvas is None:
                print("You do not have a canvas. Create a new canvas:")
                height = get_int_input("Enter height: ", 1)
                width = get_int_input("Enter width: ", 1)
                canvas = Canvas(width, height)

            filename = input("Enter the filename to export (e.g., canvas.txt): ")
            with open(filename, 'w') as file:
                for row in canvas.state:
                    file.write(''.join(row) + '\n')
            print(f"Canvas exported to file {filename}.")

        elif choice == 6:
            filename = input("Enter the filename to import (e.g., canvas.txt): ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    if canvas is None:
                        height = len(lines)
                        width = max(len(line.strip()) for line in lines)
                        canvas = Canvas(width, height)

                    for i, line in enumerate(lines):
                        canvas.state[i] = list(line.strip())
                print(f"Canvas imported from file {filename}.")
                canvas.display()
            except FileNotFoundError:
                print("File not found. Please check the filename.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == 7:
            print("Choose a symbol color:")
            for color in ANSI_COLORS.keys():
                print(color)
            color_choice = input("Enter color: ")
            if color_choice in ANSI_COLORS:
                canvas.set_symbol_color(color_choice)
                print(f"Symbol color changed to {color_choice}.")
            else:
                print("Invalid color choice.")

        elif choice == 8:
            print("Choose a background color:")
            for color in ANSI_COLORS.keys():
                print(color)
            color_choice = input("Enter color: ")
            if color_choice in ANSI_COLORS:
                canvas.set_background_color(color_choice)
                print(f"Background color changed to {color_choice}.")
            else:
                print("Invalid color choice.")

        elif choice == 9:
            canvas.undo()
            print("Last action undone.")
            canvas.display()

        elif choice == 10:
            canvas.redo()
            print("Returned to the last action.")
            canvas.display()

if __name__ == '__main__':
    main()