import time
from ae_python.standalone_functions import *
from ae_python.property import *
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
        self.properties = []

        self.properties.append(["name", Property(kwargs.get("name"))])

        self.properties.append(["position", Property(kwargs.get("position"))])

        self.properties.append(["comment", Property(kwargs.get("comment"))])
        self.properties.append(["label", Property(kwargs.get("label"))])
        self.properties.append(["locked", Property(kwargs.get("locked", False))])
        self.properties.append(["shy", Property(kwargs.get("shy", False))])
        self.properties.append(["solo", Property(kwargs.get("solo", False))])
        self.properties.append(["start_time", Property(kwargs.get("start_time", 0))])
        self.properties.append(["stretch", Property(kwargs.get("stretch"))])
        self.properties.append(["duration", Property(kwargs.get("duration"))])
        self.properties.append(["scale", Property(kwargs.get("scale"))])

        self.properties.append(["in_point", Property(kwargs.get("in_point"))])
        self.properties.append(["out_point", Property(kwargs.get("out_point"))])

        # The variable name in javascript. The name is hashed.
        self.js_variable_name: str = hash_maker()

    """
    Returns the JS variable name. 

    :return: The JS variable name. Note: the variable name is hashed and not for user interaction.
    """
    def __str__(self):
        return self.js_variable_name

    """
    Gets a property of the layer by the name.
    
    :parameter name: The name of the property. 
    
    :returns: Returns a property pointer identified by the name of the property.  
    """
    def getProperty(self, name):
        for property in self.properties:
            if property[0] == name:
                return property[1]

    """
    Deletes a property by name. 
    
    :parameter name: The name of the property. 
    """
    def deleteProperty(self, name):
        for i in range(len(self.properties)):
            if self.properties[i][0] == name:
                return self.properties.pop(i)

    """
    Sets a property by name. At first the method tries to delete the property to prevent property doubling 
    
    :parameter name: The property name you want to set.
    :parameter property: The actual property, type is property class. 
    """
    def setProperty(self, name, property):
        self.deleteProperty(name)
        self.properties.append([name, property])
