from comp import Comp
from layer import Layer
import secrets

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    """
    The hash maker creates a hash for the variable name in javascript. By this code you can call the function. The 
    code is javascript variable name save, so no syntax error can happen, cause a bad letter or character.
    """
    @staticmethod
    def __hash_maker__():
        return secrets.token_urlsafe(8).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j").replace("-", "k").replace("_", "l")

    def __create_layer__(self, layer: Layer, comp: Comp):
        layer.js_variable_name = self.__hash_maker__()
        self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addSolid([0, 0, 0], 'Distortion', 1920, 1080, 1.0);"

    # Creates a comp in javascript, it will add to js_script string.
    def __create_comp__(self, comp: Comp):
        comp.js_variable_name = self.__hash_maker__()
        self.js_script += f"var {comp.js_variable_name} = app.project.items.addComp('{comp.name}', {comp.width}, {comp.height}, {comp.pixel_aspect}, {comp.duration}, {comp.framerate});"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp)

        return self.js_script