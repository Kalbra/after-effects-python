from colour import Color
from ae_python.layer.layer import Layer

class SolidLayer(Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.color = kwargs.get("color", Color("black"))

