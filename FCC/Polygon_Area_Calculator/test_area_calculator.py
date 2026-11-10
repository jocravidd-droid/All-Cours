import pytest
from area_calculator import Rectangle, Square


def test_rectangle():
    rectangle = Rectangle(10, 5)

    assert rectangle.width == 10
    assert rectangle.height == 5
    assert rectangle.get_area() == 50
    assert rectangle.get_perimeter() == 30
    assert rectangle.get_diagonal() == pytest.approx(11.18034)
    assert rectangle.get_amount_inside(Rectangle(2, 2)) == 10
    assert str(rectangle) == "Rectangle(width=10, height=5)"

    rectangle.set_width(20)
    rectangle.set_height(10)

    assert rectangle.width == 20
    assert rectangle.height == 10


def test_square():
    square = Square(5)

    assert square.width == 5
    assert square.height == 5
    assert square.get_area() == 25
    assert square.get_perimeter() == 20
    assert square.get_diagonal() == pytest.approx(7.07107)
    assert str(square) == "Square(side=5)"

    square.set_width(8)
    assert square.width == 8
    assert square.height == 8

    square.set_height(4)
    assert square.width == 4
    assert square.height == 4

    square.set_side(6)
    assert square.width == 6
    assert square.height == 6


def test_get_picture():
    rectangle = Rectangle(3, 2)

    assert rectangle.get_picture() == "***\n***\n"
    assert Rectangle(51, 2).get_picture() == "Too big for picture."


def test_get_amount_inside():
    rectangle = Rectangle(10, 10)
    square = Square(3)

    assert rectangle.get_amount_inside(square) == 9


if __name__ == "__main__":
    pytest.main(["-v", __file__])
