import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side


if __name__ == "__main__":
    rectangle = Rectangle(10, 5)

    rectangle.set_width(20)
    rectangle.set_height(10)

    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    print(rectangle.get_diagonal())
    print(rectangle.get_picture())
    print(rectangle.get_amount_inside(Rectangle(2, 2)))
    print(rectangle)

    square = Square(5)

    square.set_width(8)
    square.set_height(4)
    square.set_side(6)

    print(square.get_area())
    print(square.get_perimeter())
    print(square.get_diagonal())
    print(square.get_picture())
    print(square.get_amount_inside(Rectangle(2, 2)))
    print(square)
