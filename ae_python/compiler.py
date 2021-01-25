from ae_python.comp import Comp
from ae_python.layer.soild_layer import SolidLayer
from ae_python.layer.null_layer import NullLayer

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    """
    Compile the layers to javascript for after effects. The layer needs the comp variable(hashed value) to add a layer 
    to the comp. Also a layer variable will be created(hashed value).
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

        # JS script for solid layer. To identify the type of the layer the class will be identified.
        if type(layer) == SolidLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addSolid([" \
                              f"{layer.color.red}, "", 100,100,1);"

        elif type(layer) == NullLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addNull();"

        else:
            raise ValueError("Class type is not in compiler list.")

        # Adds properties to layer.
        # Sets the position
        self.js_script += f"{layer.js_variable_name}.position.setValue([{layer.position[0]}, {layer.position[1]}, " \
                          f"{layer.position[2]}]);"

        # Sets the name
        self.js_script += f"{layer.js_variable_name}.name = '{layer.name}';"

        # Sets the size
        self.js_script += f"{layer.js_variable_name}.width = {layer.width}"
        self.js_script += f"{layer.js_variable_name}.height = {layer.height}"


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