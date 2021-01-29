from ae_python.property import *
from ae_python.standalone_functions import hash_maker
from typing import List
from colour import Color


class Shape:
    """
    With this class you can create shapes. It is the parent class for the different shape types.

    :parameter name: The name of the rectangle group.
    """
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")

        self.properties = []

        self.properties.append(["color", Property(kwargs.get("color", Color("blue")))])
        self.properties.append(["opacity", Property(kwargs.get("opacity", 100))])


        # The variable name in javascript. The name is hashed.
        self.js_variable_name: str = hash_maker()

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
