import unittest
from canvas import Canvas
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.triangle import Triangle
from ansi_colors import ANSI_COLORS

class TestCanvas(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(10, 10)

    def test_init_canvas(self):
        self.assertEqual(self.canvas.width, 10)
        self.assertEqual(self.canvas.height, 10)
        self.assertEqual(len(self.canvas.state), 10)
        self.assertEqual(len(self.canvas.state[0]), 10)

    def test_draw_rectangle(self):
        rectangle = Rectangle(2, 2, 5, 5)
        self.canvas.draw_figure(rectangle)
        self.assertEqual(self.canvas.figures[0].id, 1)
        self.assertEqual(self.canvas.state[2][1], ANSI_COLORS["red"] + '*'+ ANSI_COLORS["reset"] )
        self.assertEqual(self.canvas.state[4][4], ANSI_COLORS["red"] + '*'+ ANSI_COLORS["reset"] )

    def test_remove_figure(self):
        rectangle = Rectangle(2, 2, 5, 5)
        self.canvas.draw_figure(rectangle)
        self.canvas.remove_figure(1)
        self.assertEqual(len(self.canvas.figures), 0)

    def test_move_rectangle(self):
        rectangle = Rectangle(2, 2, 5, 5)
        self.canvas.draw_figure(rectangle)
        self.canvas.move_figure(1, (3, 3, 6, 6))
        self.assertEqual(self.canvas.figures[0].x1, 3)
        self.assertEqual(self.canvas.figures[0].y1, 3)

    def test_undo_redo(self):
        rectangle = Rectangle(2, 2, 5, 5)
        self.canvas.draw_figure(rectangle)
        self.canvas.undo()
        self.assertEqual(len(self.canvas.figures), 0)
        self.canvas.redo()
        self.assertEqual(len(self.canvas.figures), 1)

    def test_draw_circle(self):
        circle = Circle(5, 5, 2)
        self.canvas.draw_figure(circle)
        self.assertEqual(self.canvas.figures[0].id, 1)
        self.assertEqual(self.canvas.state[5][4], ANSI_COLORS["red"] + '*'+ ANSI_COLORS["reset"] )

    def test_draw_triangle(self):
        triangle = Triangle(1, 1, 5, 5, ANSI_COLORS["red"])
        self.canvas.draw_figure(triangle)
        self.assertEqual(self.canvas.figures[0].id, 1)
        self.assertEqual(self.canvas.state[2][1], ANSI_COLORS["red"] + '*'+ ANSI_COLORS["reset"] )

if __name__ == '__main__':
    unittest.main()