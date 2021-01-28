from ae_python.layer.layer import Layer
from ae_python.property import Property
from typing import List

class ShapeLayer(Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vertices = []

    def addVertex(self, point: List[int]):
        self.vertices.append(point)