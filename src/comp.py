from layer import Layer

class Comp:
    def __init__(self, name: str):
        self.name = name
        self.layers = []

    def addLayer(self, layer: Layer):
        self.layers.append(layer)