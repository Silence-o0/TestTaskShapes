from abc import ABC, abstractmethod


class ShapeInterface(ABC):
    shape_name = None

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def find_perimeter(self):
        pass

    @classmethod
    def read_from_line(cls, data):
        pass


class Square(ShapeInterface):
    shape_name = "Square"
    def __init__(self, point, side):
        self.top_right = point
        self.side = side
    
    def find_area(self):
        return self.side * self.side

    def find_perimeter(self):
        return self.side * 4
    
    @classmethod
    def read_from_line(cls, data):
        try:
            top_right_idx = data.index("TopRight")
            x = float(data[top_right_idx + 1])
            y = float(data[top_right_idx + 2])

            side_idx = data.index("Side")
            side = float(data[side_idx + 1])
        except(ValueError, IndexError) as e:
            raise ValueError(f"Invalid data. {cls.shape_name} should contain TopRight point and Side length.\
                             Example: Square TopRight 1 1 Side 1")
        
        if side < 0:
            raise ValueError("Side length can't be negative.")

        return cls((x, y), side)


class Rectangle(ShapeInterface):
    shape_name = "Rectangle"
    def __init__(self, point1, point2):
        self.top_right = point1
        self.bottom_left = point2
        self.side1 = abs(self.top_right[0] - self.bottom_left[0])
        self.side2 = abs(self.top_right[1] - self.bottom_left[1])
    
    def find_area(self):
        return self.side1 * self.side2

    def find_perimeter(self):
        return (self.side1 + self.side2) * 2
    
    @classmethod
    def read_from_line(cls, data):
        try:
            top_right_idx = data.index("TopRight")
            x1 = float(data[top_right_idx + 1])
            y1 = float(data[top_right_idx + 2])

            bottom_left_idx = data.index("BottomLeft")
            x2 = float(data[bottom_left_idx + 1])
            y2 = float(data[bottom_left_idx + 2])
        except(ValueError, IndexError) as e:
            raise ValueError(f"Invalid data. {cls.shape_name} should contain TopRight point and BottomLeft.\
                             Example: Rectangle TopRight 1 1 BottomLeft 2 2")

        return cls((x1, y1), (x2, y2))


class Circle(ShapeInterface):
    shape_name = "Circle"
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius
    
    def find_area(self):
        return 3.14 * (self.radius ** 2)

    def find_perimeter(self):
        return 3.14 * self.radius * 2
    
    @classmethod
    def read_from_line(cls, data):
        try:
            center_idx = data.index("Center")
            x = float(data[center_idx + 1])
            y = float(data[center_idx + 2])

            radius_idx = data.index("Radius")
            radius = float(data[radius_idx + 1])
        except(ValueError, IndexError) as e:
            raise ValueError(f"Invalid data. {cls.shape_name} should contain Center point and Radius.\
                             Example: Circle Center 1 1 Radius 2")
        
        if radius < 0:
            raise ValueError("Radius length can't be negative.")

        return cls((x, y), radius)