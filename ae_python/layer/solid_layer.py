from colour import Color
from ae_python.layer.layer import Layer
from ae_python.property import Property

class SolidLayer(Layer):
    """
    The solid layer class, you can create a solid plane with it.

    :parameter color: The color of the plane.
    :parameter pixel_aspect: The pixel_aspect of the solid.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.properties.append(["color", Property(kwargs.get("zoom", Color("black")))])
        self.properties.append(["pixel_aspect", Property(kwargs.get("pixel_aspect"))])

