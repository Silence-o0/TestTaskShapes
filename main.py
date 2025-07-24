from shapes import *


shapes_dict = {
    Square.shape_name: Square,
    Rectangle.shape_name: Rectangle,
    Circle.shape_name: Circle,
}


def compute_and_output(shapes_data):
    for shape in shapes_data:
        print(f"{shape.shape_name} Perimeter {round(shape.find_perimeter(), 2)} Area {round(shape.find_area(), 2)}")


def read_data(filename):
    shapes_obj = []

    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            shape_type, data = line[0], line[1:]

            cls = shapes_dict.get(shape_type)
            if cls is not None:
                shapes_obj.append(cls.read_from_line(data))
            else:
                raise ValueError(f"Unknown shape type: {shape_type}")
            
    return shapes_obj
           

if __name__ == '__main__':
    objects = read_data("input.txt")
    compute_and_output(objects)

