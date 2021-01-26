from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import layer
from ae_python.layer.soild_layer import SolidLayer
from ae_python.layer.text_layer import TextLayer
from colour import Color

after_effects_script = AEScript()

composition = Comp(name="hello")
composition.addLayer(SolidLayer(name="sir", position=[3,4,3], label=2, locked=True, comment="This is a comment", color=Color("blue")))
composition.addLayer(TextLayer(name="hello", font_family="Calibri", font_color=Color("blue"), font_size=40))

after_effects_script.addComp(composition)

after_effects_script.compile()