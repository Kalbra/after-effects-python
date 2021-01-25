import secrets

"""
The hash maker creates a hash for the variable name in javascript. By this code you can call the function. The 
code is javascript variable name save, so no syntax error can happen, cause a bad letter or character.
The hashing is important because if you have the following scenario:

composition = comp.Comp(name="comp1")
composition.addLayer(layer.Layer("layer1"))
composition = comp.Comp(name="comp2")
composition.addLayer(layer.Layer("layer1"))

The name "layer1" is dobbed, so the program doesn't work well, therefore the hash is used.
"""
def hash_maker():
    return secrets.token_urlsafe(8).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j").replace("-", "k").replace("_", "l")
