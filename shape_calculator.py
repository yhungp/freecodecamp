class shape_calculator():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def __repr__(self):
            return "Rectangle(width={w}, height={h})".format(h=self.height,
                                                                     w=self.width)

        def get_area(self):
            return self.width * self.height

        def get_perimeter(self):
            return 2 * self.width + 2 * self.height

        def get_picture(self):
            if self.width > 50 or self.height > 50: return "Too big for picture."
            return "\n".join(["*" * self.width for i in range(self.height)])

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            self.height = height

        def get_diagonal(self):
            return (self.width ** 2 + self.height ** 2) ** .5

        def get_amount_inside(self, shape):
            return int(self.get_area() / shape.get_area())
            
    class Square(Rectangle):
        def __init__(self, side):
            super().__init__(side, side)
            self.side = side

        def __repr__(self):
            return "Square(side={s})".format(s=self.side)

        def set_side(self, side):
            self.side = side
            super().__init__(side, side)

        def set_width(self, side):
            self.side = side
            super().__init__(side, side)

        def set_height(self, side):
            self.side = side
            super().__init__(side, side)
