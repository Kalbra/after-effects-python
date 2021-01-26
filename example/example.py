from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import SolidLayer
from ae_python.layer import TextLayer
from colour import Color

after_effects_script = AEScript()

composition = Comp(name="hello")
composition.addLayer(SolidLayer(name="sir", label=2, locked=True, comment="This is a comment", color=Color("blue")))
composition.addLayer(TextLayer(name="hello", font_family="Calibri", font_color=Color("blue"), font_size=40))

after_effects_script.addComp(composition)

after_effects_script.compile()