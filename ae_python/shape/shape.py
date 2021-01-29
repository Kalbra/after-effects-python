from ae_python.property import *
from typing import List
from colour import Color

class Shape:
    """
    With this class you can create shapes. You can add points to make a shape.

    :parameter points: Set the point and tangents in the following format:
                    [ [ [point], [in], [out] ], [ [point], [in], [out] ] ]
    :parameter closed: When true, the first and last vertices are connected to form a closed curve. When false, the
                       closing segment is not drawn.
    """
    def __init__(self, *args, **kwargs):
        self.properties = []

        self.properties.append(["color", Property(kwargs.get("color", Color("blue")))])



