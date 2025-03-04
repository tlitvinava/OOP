from tkinter import PhotoImage

class Background:
    def __init__(self, params):
        self.params = params
        self.image_path = params.get('image_path')
        self.color = params.get('color')

    def apply(self, canvas):
        if self.image_path:
            self.set_image_background(canvas)
        elif self.color:
            self.set_color_background(canvas)

    def set_image_background(self, canvas):
        self.image = PhotoImage(file=self.image_path)
        canvas.create_image(0, 0, anchor='nw', image=self.image)
        canvas.lower(self.image)  # Поместить изображение на задний план

    def set_color_background(self, canvas):
        canvas.config(bg=self.color)
        canvas.lower(self.color)  # Поместить цвет на задний план
