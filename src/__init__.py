import ae_script, comp

after_effects_script = ae_script.AEScript()

after_effects_script.addComp(comp.Comp("helo"))

after_effects_script.render()