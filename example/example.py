from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import layer
from ae_python.layer.soild_layer import SolidLayer

after_effects_script = AEScript()

composition = Comp(name="hello")
composition.addLayer(SolidLayer(name="sir", position=[3,4,3]))

after_effects_script.addComp(composition)

after_effects_script.compile()