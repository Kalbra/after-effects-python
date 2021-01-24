import time

class Layer:
    def __init__(self, name: str):
        self.name = name

        self.start_time: float = 0

        # The variable name in javascript. The name is hashed.
        self.js_variable_name = ""
