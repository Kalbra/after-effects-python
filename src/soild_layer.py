from colour import Color
from layer import Layer

class SolidLayer(Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.color = kwargs.get("color", Color("black"))

