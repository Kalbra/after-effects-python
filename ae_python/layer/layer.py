import time
from ae_python.standalone_functions import *
from typing import List

class Layer:
    """
    The parent class for all layer types. Contains basic values.

    :parameter name: A string containing the name of the solid.

    :parameter position: The position of the layer(on the top left corner). Needs array in following style: [x, y, z]

    :parameter comment: A descriptive comment for the layer.
    :parameter label: The label color for the item. Colors are represented by their number (0 for None, or 1 to 16 for
                      one of the preset colors in the Labels preferences).
    :parameter locked: When true, the layer is locked; otherwise false. This corresponds to the lock toggle in the Layer
                       panel.
    :parameter shy: When true, the layer is “shy”, meaning that it is hidden in the Layer panel if the composition’s
                    “Hide all shy layers” option is toggled on.
    :parameter solo: When true, the layer is soloed, otherwise false.
    :parameter start_time: The time when the layer starts.
    :parameter stretch: The layer’s time stretch, expressed as a percentage. A value of 100 means no stretch. Values
                        between 0 and 1 are set to 1, and values between -1 and 0 (not including 0) are set to -1.
    :parameter duration: Optional, the length of a still layer in seconds, a floating-point value.
    :parameter scale: The scale of the layer.

    :parameter in_point: The “in” point of the layer, expressed in composition time (seconds).
    :parameter out_point: The “out” point of the layer, expressed in composition time (seconds).
    """
    def __init__(self, *args, **kwargs):
        self.name: str = kwargs.get("name")

        self.position: List[int] = kwargs.get("position", [0, 0, 0])

        self.comment: str = kwargs.get("comment")
        self.label: int = kwargs.get("label")
        self.locked: bool = kwargs.get("locked", False)
        self.shy: bool = kwargs.get("shy", False)
        self.solo: bool = kwargs.get("solo", False)
        self.start_time: float = kwargs.get("start_time", 0)
        self.stretch: float = kwargs.get("stretch")
        self.duration: float = kwargs.get("duration")
        self.scale: float = kwargs.get("scale")

        self.in_point: float = kwargs.get("in_point")
        self.out_point: float = kwargs.get("out_point")

        # The variable name in javascript. The name is hashed.
        self.js_variable_name = hash_maker()

    """
    Returns the JS variable name. 
    
    :return: The JS variable name. Note: the variable name is hashed and not for user interaction.
    """
    def __str__(self):
        return self.js_variable_name
