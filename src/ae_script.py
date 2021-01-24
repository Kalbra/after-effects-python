from comp import Comp
from render import Render

class AEScript:

    def __init__(self):
        self.comp_list = []

    def addComp(self, comp: Comp):
        self.comp_list.append(comp)

    def __create_layer__(self):
        pass

    def render(self):
        render_class = Render(self.comp_list).render()