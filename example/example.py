from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import SolidLayer
from ae_python.layer import TextLayer
from ae_python.property import *
from colour import Color

after_effects_script = AEScript()

composition = Comp(name="Hello World - Example")


position_property = Property([0, 0, 0])
position_property.setValueAtTime(0, [0, 0, 0])
position_property.setValueAtTime(1, [200, 200, 0])
position_property.setValueAtTime(2, [100, 600, 0])
position_property.setValueAtTime(3, [300, 400, 0])
position_property.setValueAtTime(4, [900, 200, 0])
position_property.setValueAtTime(5, [0, 100, 0])
position_property.setValueAtTime(6, [100, 600, 0])
position_property.setValueAtTime(7, [600, 300, 0])
position_property.setValueAtTime(8, [400, 500, 0])


color_property = Property(Color("white"))
color_property.setValueAtTime(0, Color("red"))
color_property.setValueAtTime(1, Color("green"))
color_property.setValueAtTime(2, Color("blue"))
color_property.setValueAtTime(3, Color("lime"))
color_property.setValueAtTime(4, Color("yellow"))
color_property.setValueAtTime(5, Color("white"))


layer = TextLayer(name="Hello", font_family="Calibri", font_color=Color("blue"), font_size=40, position=position_property)

composition.addLayer(SolidLayer(name="sir", label=2, locked=True, comment="This is a comment", color=Color("blue")))
composition.addLayer(layer)

after_effects_script.addComp(composition)

after_effects_script.compile()