from layer import Layer

class NullLayer(Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)