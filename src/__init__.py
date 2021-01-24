import ae_script, comp, layer


after_effects_script = ae_script.AEScript()



composition = comp.Comp("helo")
composition.addLayer(layer.Layer("dsf"))
composition.addLayer(layer.Layer("dsf"))

after_effects_script.addComp(composition)

after_effects_script.compile()