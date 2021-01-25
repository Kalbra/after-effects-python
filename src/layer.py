import time
from standalone_functions import *
class Layer:
    """
    The parent class for all layer types. Contains basic values.

    :parameter name: A string containing the name of the solid.
    :parameter start_time: The time when the layer starts.
    :parameter duration: Optional, the length of a still layer in seconds, a floating-point value.
    :parameter pixel_aspect:  	The pixel aspect ratio of the solid, a floating-point value in the range [0.01..100.0].
    :parameter position: The position of the layer(on the top left corner). Needs array in following style: [x, y, z]
    :parameter width: The width of the solid in pixels, an integer in the range [4..30000].
    :parameter height: The height of the solid in pixels, an integer in the range [4..30000].
    """
    def __init__(self, *args, **kwargs):
        self.name: str = kwargs.get("name")
        self.start_time: float = kwargs.get("start_time", 0)
        self.duration: float = kwargs.get("duration")
        self.pixel_aspect: float = kwargs.get("pixel_aspect")

        self.x = kwargs.get("position", [0,0,0])[0]
        self.y = kwargs.get("position", [0,0,0])[1]
        self.z = kwargs.get("position", [0,0,0])[2]
        
        self.width = kwargs.get("width")
        self.height = kwargs.get("height")

        # The variable name in javascript. The name is hashed.
        self.js_variable_name = hash_maker()
