import ae_script, comp, layer
from soild_layer import SolidLayer

after_effects_script = ae_script.AEScript()

composition = comp.Comp(name="hello")
composition.addLayer(SolidLayer(name="sir"))
composition.addLayer(layer.Layer(name="dsf"))

after_effects_script.addComp(composition)

after_effects_script.compile()
