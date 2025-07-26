import pytest
from shapes import *


# Square tests

def test_square_valid_computing():
    shape = Square((2, 2), 5)
    assert shape.find_area() == 25
    assert shape.find_perimeter() == 20

def test_square_valid_read_from_line():
    data = ["TopRight", "2", "3", "Side", "4"]
    shape = Square.read_from_line(data)
    assert shape.top_right == (2, 3)
    assert shape.side == 4

def test_square_invalid_missing_topright():
    data = ["Side", "4"]
    with pytest.raises(ValueError):
        Square.read_from_line(data)

def test_square_invalid_missing_side():
    data = ["TopRight", "2", "3"]
    with pytest.raises(ValueError):
        Square.read_from_line(data)

def test_square_invalid_negative_side():
    data = ["TopRight", "1", "1", "Side", "-5"]
    with pytest.raises(ValueError):
        Square.read_from_line(data)


# Rectangle tests

def test_rectangle_valid_computing():
    shape = Rectangle((3, 4), (1, 1))
    assert shape.find_area() == 6
    assert shape.find_perimeter() == 10

def test_rectangle_valid_read_from_line():
    data = ["TopRight", "3", "4", "BottomLeft", "1", "1"]
    shape = Rectangle.read_from_line(data)
    assert shape.top_right == (3, 4)
    assert shape.bottom_left == (1, 1)

def test_rectangle_invalid_missing_topright():
    data = ["BottomLeft", "1", "1"]
    with pytest.raises(ValueError):
        Rectangle.read_from_line(data)

def test_rectangle_invalid_missing_bottomleft():
    data = ["TopRight", "3", "3"]
    with pytest.raises(ValueError):
        Rectangle.read_from_line(data)


# Circle tests

def test_circle_valid_computing():
    shape = Circle((1, 1), 5)
    assert shape.find_area() == pytest.approx(78.5, 1)
    assert shape.find_perimeter() == pytest.approx(31.4, 1)

def test_circle_valid_read_from_line():
    data = ["Center", "1", "1", "Radius", "5"]
    shape = Circle.read_from_line(data)
    assert shape.center == (1, 1)
    assert shape.radius == 5

def test_circle_invalid_missing_center():
    data = ["Radius", "5"]
    with pytest.raises(ValueError):
        Circle.read_from_line(data)

def test_circle_invalid_missing_radius():
    data = ["Center", "1", "1"]
    with pytest.raises(ValueError):
        Circle.read_from_line(data)

def test_circle_invalid_negative_radius():
    data = ["Center", "1", "1", "Radius", "-5"]
    with pytest.raises(ValueError):
        Circle.read_from_line(data)


# Triangle tests

def test_triangle_valid_computing():
    shape = Triangle((3, 4), (1, 1), (0, 0))
    assert shape.find_area() == pytest.approx(0.5, 1)
    assert shape.find_perimeter() == pytest.approx(10, 1)

def test_triangle_valid_computing2():
    shape = Triangle((2, 2), (1, 1), (8, 10))
    assert shape.find_area() == pytest.approx(1, 1)
    assert shape.find_perimeter() == pytest.approx(22.8, 1)

def test_triangle_valid_read_from_line():
    data = ["Point1", "3", "4", "Point2", "1", "1", "Point3", "0", "0"]
    shape = Triangle.read_from_line(data)
    assert shape.point1 == (3, 4)
    assert shape.point2 == (1, 1)
    assert shape.point3 == (0, 0)

# def test_rectangle_invalid_missing_topright():
#     data = ["BottomLeft", "1", "1"]
#     with pytest.raises(ValueError):
#         Rectangle.read_from_line(data)

# def test_rectangle_invalid_missing_bottomleft():
#     data = ["TopRight", "3", "3"]
#     with pytest.raises(ValueError):
#         Rectangle.read_from_line(data)