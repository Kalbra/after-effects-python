from ae_python.shape.shape import Shape
from ae_python.property import Property


class Ellipse(Shape):
    """
    Make a new ellipse shape.

    :parameter size: The size of the rectangle, is a array of the following format: [width, height].
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.properties.append(["size", Property(kwargs.get("size", [100, 100]))])




