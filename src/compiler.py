from comp import Comp
from layer import Layer

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    def __create_layer__(self, layer: Layer, comp_name: str):
        print(comp_name)

    def __create_comp__(self, comp: Comp):
        self.js_script += f"app.project.items.addComp('{comp.name}');"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp.name)



        print(self.js_script)