from ae_python.layer.layer import Layer
from ae_python.property import Property
from typing import List

class ShapeLayer(Layer):
    """
    The shape layer class, child of layer. You can add shapes like ellipse, rectangle or path/vetor.

    :parameter shapes: Array of the shapes you want to add.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shapes = kwargs.get("shapes", [])

    """
    Adds a shape to the shape layer.
    
    :parameter shape: The shape you want to add. 
    """
    def addShape(self, shape):
        self.shapes.append(shape)