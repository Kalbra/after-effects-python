from ae_python.comp import Comp
from ae_python.compiler import Compiler
import os

"""
The AEScript class contains a script. You can add Comps by using addComp(), the comps contain layers where the 
creative stuff happen. 
"""
class AEScript:
    """
    The constructor of the class. It creates a list of comps. Note that the comp list is at first empty, but you can
    add comps via addComp().
    """
    def __init__(self):
        self.comp_list = []

    """
    Add a comp class to the script. 

    :parameter: Comp class that will be added to the script.
    """
    def addComp(self, comp: Comp):
        self.comp_list.append(comp)

    """
    Compile the given things. Compile means the python objects will be converted into javascript what after effects can 
    read.
    """
    def compile(self):
        # Run the compiler and saves it into js_respond
        js_respond = Compiler(self.comp_list).compile()

        # Add standard function at the first of the js_respond
        js_respond = open(f"{os.path.dirname(__file__)}/js/std_functions.js", "r").read() + js_respond

        output_file = open("python_js_script.js", "w")
        output_file.write(js_respond)
        output_file.close()

        # Debug call
        print(js_respond)