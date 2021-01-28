from ae_python.comp import Comp
from ae_python.layer.solid_layer import SolidLayer
from ae_python.layer.null_layer import NullLayer
from ae_python.layer.camera_layer import CameraLayer
from ae_python.layer.text_layer import TextLayer
from ae_python.property import *

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
                              f"{layer.getProperty('color').default_value.red}," \
                              f"{layer.getProperty('color').default_value.green}," \
                              f"{layer.getProperty('color').default_value.blue}], '{layer.getProperty('name')}'," \
                              f" {comp.width}, {comp.height},1);"

        # JS script for null layer.
        elif type(layer) == NullLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addNull();"

        # JS script for camara layer.
        elif type(layer) == CameraLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addCamera('', " \
                              f"{layer.getProperty('center_point')});"

        # JS script for text layer.
        elif type(layer) == TextLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addText('" \
                              f"{layer.getProperty('text')}');var {layer.js_text_variable_name} = " \
                              f"{layer.js_variable_name}.text.sourceText.value;{layer.js_text_variable_name}.fontSize" \
                              f" = {layer.getProperty('font_size')};{layer.js_text_variable_name}.fillColor = " \
                              f"[{layer.getProperty('font_color').default_value.red}," \
                              f"{layer.getProperty('font_color').default_value.green}," \
                              f"{layer.getProperty('font_color').default_value.blue}];{layer.js_text_variable_name}" \
                              f".font = '{layer.getProperty('font_family')}';{layer.js_variable_name}" \
                              f".text.sourceText.setValue({layer.js_text_variable_name});"

        else:
            raise ValueError("Class type is not in compiler list.")

        # Adds default properties to layer.
        # Sets the position
        if layer.getProperty('position').isNone():
            layer.setProperty('position', Property([comp.middle[0], comp.middle[1], 0]))

        self.js_script += f"{layer.js_variable_name}.position.setValue([{layer.getProperty('position')[0]}, " \
                          f"{layer.getProperty('position')[1]}, {layer.getProperty('position')[2]}]);"

        # Sets the rotation
        self.js_script += f"{layer.js_variable_name}.rotation = {layer.getProperty('rotation')};"

        # Sets the name
        self.js_script += f"{layer.js_variable_name}.name = '{layer.getProperty('name')}';"

        # Sets the comment
        if not layer.getProperty('comment').isNone():
            self.js_script += f"{layer.js_variable_name}.comment = '{layer.getProperty('comment')}';"

        # Sets the label
        if not layer.getProperty('label').isNone():
            self.js_script += f"{layer.js_variable_name}.label = {layer.getProperty('label')};"

        # Sets if shy
        if layer.getProperty('shy') == 'True':
            self.js_script += f"{layer.js_variable_name}.shy = true;"

        # Sets if solo
        if layer.getProperty('solo') == 'True':
            self.js_script += f"{layer.js_variable_name}.solo = true;"

        # Sets the start time
        self.js_script += f"{layer.js_variable_name}.startTime = {layer.getProperty('start_time')};"

        # Sets the stretch
        if not layer.getProperty('stretch').isNone():
            self.js_script += f"{layer.js_variable_name}.stretch = {layer.getProperty('stretch')};"

        # Sets the in point
        if not layer.getProperty('in_point').isNone():
            self.js_script += f"{layer.js_variable_name}.inPoint = {layer.getProperty('in_point')}"

        # Sets the out point
        if not layer.getProperty('out_point').isNone():
            self.js_script += f"{layer.js_variable_name}.outPoint = {layer.getProperty('out_point')}"

        # Sets if looked. Note: Locked has to be on the end because after you lock a layer you cant edit it.
        if layer.getProperty('locked') == 'True':
            self.js_script += f"{layer.js_variable_name}.locked = true;"

        # Keyframe compiler
        for property in layer.properties:
            property_name = property[0]

            for value in property[1].value_stack:
                property_time = value[0]
                property_value = value[1]

                # Sets the position
                if property_name == "position":
                    self.js_script += f"{layer.js_variable_name}.position.setValueAtTime({property_time}, " \
                                      f"[{property_value[0]},{property_value[1]},{property_value[2]}]);"

                # Sets the comment
                elif property_name == "comment":
                    self.js_script += f"{layer.js_variable_name}.comment.setValueAtTime({property_time}, " \
                                      f"'{property_value}');"

                # Sets the label
                elif property_name == "label":
                    self.js_script += f"{layer.js_variable_name}.label.setValueAtTime({property_time}," \
                                      f"'{property_value}');"

                # Sets if shy
                elif property_name == "shy":
                    if property_value:
                        self.js_script += f"{layer.js_variable_name}.shy.setValueAtTime({property_time},true);"
                    else:
                        self.js_script += f"{layer.js_variable_name}.shy.setValueAtTime({property_time},false);"

                # Sets if solo
                elif property_name == "solo":
                    if property_value:
                        self.js_script += f"{layer.js_variable_name}.solo.setValueAtTime({property_time},true);"
                    else:
                        self.js_script += f"{layer.js_variable_name}.solo.setValueAtTime({property_time},false);"

                # Sets the stretch
                # elif property_name == "stretch":
                #     self.js_script += f""

    """
     Compile the comps to javascript for after effects. The variable name is hashed to prevent doubling 
    """
    def __create_comp__(self, comp: Comp):
        self.js_script += f"var {comp.js_variable_name} = app.project.items.addComp('{comp.name}', {comp.width}, " \
                          f"{comp.height}, {comp.pixel_aspect}, {comp.duration}, {comp.framerate});"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp)

        return self.js_script