from comp import Comp
from compiler import Compiler

"""
The AEScript class contains a script. You can add Comps by using addComp(), the comps contain layers where the 
creative stuff happen. 
"""
class AEScript:
    """
    The constructor of the class. It creates a list of comps. Note that the comp list is at first empty, but you can
    add comps via addComp()
    """
    def __init__(self):
        self.comp_list = []

    """
    Add a comp class to the script. 
    
    :parameter: Comp class that will be added to the script
    """
    def addComp(self, comp: Comp):
        self.comp_list.append(comp)

    """
    Compile the given things. Compile means the python objects will be converted into javascript what after effects can 
    read. 
    """
    def compile(self):
        render_class = Compiler(self.comp_list).compile()
