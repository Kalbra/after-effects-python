from comp import Comp
from layer import Layer
from soild_layer import SolidLayer
import secrets
from standalone_functions import *

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    """
    Compile the layers to javascript for after effects. The layer needs the comp variable(hashed value) to add a layer 
    to the comp. Also a layer variable will be created(hashed value)
    """
    def __create_layer__(self, layer, comp: Comp):
        print(type(layer))
        # If the layer size isn't set the layer size is equal to the comp size.
        if layer.height or layer.width == None:
            layer.height = comp.height
            layer.width  = comp.width

        # If the pixel aspect isn't set the layer the value is the same as in the comp
        if layer.pixel_aspect == None:
            layer.pixel_aspect = comp.pixel_aspect

        # If the duration is set it will be inserted into the js script if not the option will not be set, because the
        # option is not required.
        if layer.duration != None:
            duration_string = f", {layer.duration}"
        else:
            duration_string = ""

        # JS script for solid layer. To identify the type of the layer the class will be identified.
        if type(layer) == SolidLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addSolid([" \
                              f"{layer.color.red}, {layer.color.green}, {layer.color.blue}], '{layer.name}', " \
                              f"{layer.width}, {layer.height}, {layer.pixel_aspect}{duration_string});"

        else:
            raise ValueError("Class type is not in compiler list.")

        # Adds properties to layer.
        # Sets the position
        self.js_script += f"{layer.js_variable_name}.position.setValue([{layer.x}, {layer.y}, {layer.z}]);"

    """
     Compile the comps to javascript for after effects. The variable name is hashed to prevent doubling 
    """
    def __create_comp__(self, comp: Comp):
        self.js_script += f"var {comp.js_variable_name} = app.project.items.addComp('{comp.name}', {comp.width}, {comp.height}, {comp.pixel_aspect}, {comp.duration}, {comp.framerate});"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp)

        return self.js_script