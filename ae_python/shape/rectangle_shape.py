from ae_python.shape.shape import Shape
from ae_python.property import Property


class Rectangle(Shape):
    """
    Make a new rectangle shape.

    :parameter size: The size of the rectangle, is a array of the following format: [width, height].
    :parameter roundness: The roundness of the rectangle, default is 0.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.properties.append(["size", Property(kwargs.get("size", [100, 100]))])
        self.properties.append(["roundness", Property(kwargs.get("roundness"), 0)])
