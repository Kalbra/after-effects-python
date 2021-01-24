from comp import Comp
from layer import Layer
from soild_layer import SolidLayer
import secrets

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    """
    The hash maker creates a hash for the variable name in javascript. By this code you can call the function. The 
    code is javascript variable name save, so no syntax error can happen, cause a bad letter or character.
    The hashing is important because if you have the following scenario:
    
    composition = comp.Comp(name="comp1")
    composition.addLayer(layer.Layer("layer1"))
    composition = comp.Comp(name="comp2")
    composition.addLayer(layer.Layer("layer1"))
    
    The name "layer1" is dobbed, so the program doesn't work well, therefore the hash is used.
    """
    @staticmethod
    def __hash_maker__():
        return secrets.token_urlsafe(8).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j").replace("-", "k").replace("_", "l")

    """
    Compile the layers to javascript for after effects. The layer needs the comp variable(hashed value) to add a layer 
    to the comp. Also a layer variable will be created(hashed value)
    """
    def __create_layer__(self, layer, comp: Comp):
        layer.js_variable_name = self.__hash_maker__()
        print(type(layer))
        # If the layer size isn't set the layer size is equal to the comp size.
        if layer.height or layer.width == None:
            layer.height = comp.height
            layer.width  = comp.width

        # If the pixel aspect isn't set the layer the value is the same as in the comp
        if layer.pixel_aspect == None:
            layer.pixel_aspect = comp.pixel_aspect

        if layer.duration != None:
            duration_string = f", {layer.duration}"
        else:
            duration_string = ""

        if type(layer) == SolidLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addSolid([{layer.color.red}, {layer.color.green}, {layer.color.blue}], '{layer.name}', {layer.width}, {layer.height}, {layer.pixel_aspect}{duration_string});"

        else:
            raise ValueError("Class type is not in compiler list.")
    """
     Compile the comps to javascript for after effects. The variable name is hashed to prevent doubling 
    """
    def __create_comp__(self, comp: Comp):
        comp.js_variable_name = self.__hash_maker__()
        self.js_script += f"var {comp.js_variable_name} = app.project.items.addComp('{comp.name}', {comp.width}, {comp.height}, {comp.pixel_aspect}, {comp.duration}, {comp.framerate});"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp)

        return self.js_script