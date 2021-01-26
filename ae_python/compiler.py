from ae_python.comp import Comp
from ae_python.layer.solid_layer import SolidLayer
from ae_python.layer.null_layer import NullLayer
from ae_python.layer.camera_layer import CameraLayer
from ae_python.layer.text_layer import TextLayer

class Compiler:
    def __init__(self, comps: Comp):
        self.comp_list = comps

        self.js_script = ""

    """
    Compile the layers to javascript for after effects. The layer needs the comp variable(hashed value) to add a layer 
    to the comp. Also a layer variable will be created(hashed value).
    """
    def __create_layer__(self, layer, comp: Comp):
        # JS script for solid layer. To identify the type of the layer the class will be identified.
        if type(layer) == SolidLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addSolid([" \
                              f"{layer.color.red},{layer.color.green},{layer.color.blue}], '{layer.name}', 100,100,1);"

        # JS script for null layer.
        elif type(layer) == NullLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addNull();"

        # JS script for camara layer.
        elif type(layer) == CameraLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addCamera('', " \
                              f"{layer.center_point});"

        # JS script for text layer.
        elif type(layer) == TextLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addText('{layer.text}'" \
                              f");var {layer.js_text_variable_name} = {layer.js_variable_name}.text.sourceText.value;" \
                              f"{layer.js_text_variable_name}.fontSize = {layer.font_size};" \
                              f"{layer.js_text_variable_name}.fillColor = [{layer.font_color.red}," \
                              f"{layer.font_color.green},{layer.font_color.blue}];{layer.js_text_variable_name}.font" \
                              f" = '{layer.font_family}';{layer.js_variable_name}.text.sourceText.setValue" \
                              f"({layer.js_text_variable_name});"

        else:
            raise ValueError("Class type is not in compiler list.")

        # Adds properties to layer.
        # Sets the position
        if layer.position == None:
            layer.position = [comp.middle[0], comp.middle[1], 0]

        self.js_script += f"{layer.js_variable_name}.position.setValue([{layer.position[0]}, {layer.position[1]}, " \
                          f"{layer.position[2]}]);"

        # Sets the name
        self.js_script += f"{layer.js_variable_name}.name = '{layer.name}';"

        # Sets the comment
        if layer.comment != None:
            self.js_script += f"{layer.js_variable_name}.comment = '{layer.comment}';"

        # Sets the label
        if layer.label != None:
            self.js_script += f"{layer.js_variable_name}.label = {layer.label};"

        # Sets if shy
        if layer.shy:
            self.js_script += f"{layer.js_variable_name}.shy = true;"

        # Sets if solo
        if layer.solo:
            self.js_script += f"{layer.js_variable_name}.solo = true;"

        # Sets the start time
        self.js_script += f"{layer.js_variable_name}.startTime = {layer.start_time};"

        # Sets the stretch
        if layer.stretch != None:
            self.js_script += f"{layer.js_variable_name}.stretch = {layer.stretch};"

        # Sets the in point
        if layer.in_point != None:
            self.js_script += f"{layer.js_variable_name}.inPoint = {layer.in_point}"

        # Sets the out point
        if layer.out_point != None:
            self.js_script += f"{layer.js_variable_name}.outPoint = {layer.out_point}"

        # Sets if looked. Note: Locked has to be on the end because after you lock a layer you cant edit it.
        if layer.locked:
            self.js_script += f"{layer.js_variable_name}.locked = true;"

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