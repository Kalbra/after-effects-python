from ae_python.comp import Comp
from ae_python.layer.solid_layer import SolidLayer
from ae_python.layer.null_layer import NullLayer
from ae_python.layer.camera_layer import CameraLayer
from ae_python.layer.text_layer import TextLayer
from ae_python.layer.shape_layer import ShapeLayer
from ae_python.shape.rectangle_shape import Rectangle
from ae_python.shape.ellipse_shape import Ellipse
from ae_python.shape.path_shape import Path
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
                              f".font = '{layer.getProperty('font_family')}';"

            # @TODO: This do not work
            for value in self.__property_decoder__(layer.getProperty("font_color")):
                self.js_script += f"{layer.js_text_variable_name}.fillColor.setValueAtTime({value[0]}, [{value[1].red},{value[1].green},{value[1].blue}]);"

            self.js_script += f"{layer.js_variable_name}.text.sourceText.setValue({layer.js_text_variable_name});"

        # JS script for shape layer.
        elif type(layer) == ShapeLayer:
            self.js_script += f"var {layer.js_variable_name} = {comp.js_variable_name}.layers.addShape();"

            for shape in layer.shapes:
                # Defines the group and shape
                self.js_script += f"var {shape.js_variable_name} = {layer.js_variable_name}.property('ADBE Root " \
                                  f"Vectors Group').addProperty('ADBE Vector Group').property('ADBE Vectors Group');"

                # Set the rectangle
                if type(shape) == Rectangle:
                    self.js_script += f"{shape.js_variable_name}.addProperty('ADBE Vector Shape - Rect');"

                # Set the ellipse
                elif type(shape) == Ellipse:
                    self.js_script += f"{shape.js_variable_name}.addProperty('ADBE Vector Shape - Ellipse')"

                # Sets the fill color
                # @TODO: Add opacity and stroke to the script
                self.js_script += f"{shape.js_variable_name}.addProperty('ADBE Vector Graphic - Fill').property" \
                                  f"('ADBE Vector Fill Color').setValue([" \
                                  f"{shape.getProperty('color').default_value.red}," \
                                  f"{shape.getProperty('color').default_value.green}," \
                                  f"{shape.getProperty('color').default_value.blue}]);"

        else:
            raise ValueError("Class type is not in compiler list.")

        # Adds default properties to layer.
        # Sets the position
        if layer.getProperty('position').isNone():
            layer.setProperty('position', Property([comp.middle[0], comp.middle[1], 0]))

        self.js_script += f"{layer.js_variable_name}.position.setValue([{layer.getProperty('position')[0]}, " \
                          f"{layer.getProperty('position')[1]}, {layer.getProperty('position')[2]}]);"

        for value in self.__property_decoder__(layer.getProperty("position")):
            self.js_script += f"{layer.js_variable_name}.position.setValueAtTime({value[0]}, [{value[1][0]}," \
                              f"{value[1][1]},{value[1][2]}]);"

        # Sets the rotation
        self.js_script += f"{layer.js_variable_name}.rotation = {layer.getProperty('rotation')};"

        for value in self.__property_decoder__(layer.getProperty("rotation")):
            self.js_script = f"{layer.js_variable_name}.position.setValueAtTime({value[0]}, {value[1]});"

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
            self.js_script += f"{layer.js_variable_name}.inPoint = {layer.getProperty('in_point')};"

        # Sets the out point
        if not layer.getProperty('out_point').isNone():
            self.js_script += f"{layer.js_variable_name}.outPoint = {layer.getProperty('out_point')};"

        # Sets if looked. Note: Locked has to be on the end because after you lock a layer you cant edit it.
        if layer.getProperty('locked') == 'True':
            self.js_script += f"{layer.js_variable_name}.locked = true;"


    """
    Gets the property values(name, time, script)
    
    :parameter property: The property you want to decode.
    
    :returns: Returns an array in the following order [time, value] 
    """
    def __property_decoder__(self, property):
        for value in property.value_stack:
            property_time = value[0]
            property_value = value[1]

            yield property_time, property_value

    """
     Compile the comps to javascript for after effects. The variable name is hashed to prevent doubling 
    """
    def __create_comp__(self, comp: Comp):
        self.js_script += f"var {comp.js_variable_name} = app.project.items.addComp('{comp.name}', {comp.width}, " \
                          f"{comp.height}, {comp.pixel_aspect}, {comp.duration}, {comp.framerate});" \
                          f"{comp.js_variable_name}.label = {comp.label};"

        if comp.comment != None:
            self.js_script += f"{comp.js_variable_name}.comment = '{comp.comment}';"

    def compile(self):
        for comp in self.comp_list:
            self.__create_comp__(comp)

            for layer in comp.layers:
                self.__create_layer__(layer, comp)

        return self.js_script