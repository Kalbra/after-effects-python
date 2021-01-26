from ae_python.layer.layer import Layer
from ae_python.standalone_functions import *

class Comp:
    """
    Constructor of comp. Has all comp options see:
    https://after-effects-scripting-guide.readthedocs.io/items/itemcollection/#itemcollection-addcomp

    :parameter name: A string containing the name of the composition.
    :parameter width: The width of the composition in pixels, an integer in the range [4..30000].
    :parameter height: The height of the composition in pixels, an integer in the range [4..30000].
    :parameter pixel_aspect: The pixel aspect ratio of the composition, a floating-point value in the
                             range [0.01..100.0].
    :parameter duration: The duration of the composition in seconds, a floating-point value in the range [0.0..10800.0].
    :parameter framerate: The frame rate of the composition, a floating-point value in the range [1.0..99.0].
    """
    def __init__(self, *args, **kwargs):
        self.name: str = kwargs.get("name")
        self.width: int = kwargs.get("width", 1280)
        self.height: int = kwargs.get("height", 720)
        self.pixel_aspect: float = kwargs.get("pixel_aspect", 1.78)
        self.duration: float = kwargs.get("duration", 30.0)
        self.framerate: float = kwargs.get("framerate", 30.0)

        # Layer list for the layers. At first empty, you can add a layer via addLayer()
        self.layers = []

        # The variable name in javascript. The name is hashed.
        self.js_variable_name:str  = hash_maker()

        # Sets the middle point of the comp. It is a position, so [x,y].
        self.middle: int = [self.width/2, self.height/2]


    def addLayer(self, layer: Layer):
        self.layers.append(layer)