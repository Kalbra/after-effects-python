from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import SolidLayer
from ae_python.layer import TextLayer
from ae_python.property import *
from colour import Color

after_effects_script = AEScript()

composition = Comp(name="hello")


property = Property("world")
property.setValueAtTime(0, "hello")
property.setValueAtTime(1, "dfdfds")


layer = TextLayer(name=property, font_family="Calibri", font_color=Color("blue"), font_size=40)

composition.addLayer(SolidLayer(name="sir", label=2, locked=True, comment="This is a comment", color=Color("blue")))
composition.addLayer(layer)

after_effects_script.addComp(composition)

after_effects_script.compile()