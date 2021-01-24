from comp import Comp
from layer import Layer

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    def __create_layer__(self, layer: Layer, comp_name: str):
        print(comp_name)

    # Creates a comp in javascript, it will add to js_script string.
    def __create_comp__(self, comp: Comp):
        self.js_script += f"app.project.items.addComp('{comp.name}, {comp.width}, {comp.height}, {comp.pixel_aspect}," \
                          f" {comp.duration}, {comp.framerate}');"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp.name)

        return self.js_script