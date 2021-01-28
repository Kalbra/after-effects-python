class Property:
    def __init__(self, default_value):
        # If the type is property so this class not a subclass will be created the values will be transfer.
        if type(default_value) == Property:
            self.default_value = default_value.default_value
            self.value_stack = default_value.value_stack

        else:
            self.default_value = default_value

            # The value stack is 3D array to set values at given times. This is needed to make animations. The array
            # subarray is in the following format: [time, value]
            self.value_stack = []

    """
    With this method you can set a keyframe at a given time, so it is possible to make animation or changes over time.
    
    :parameter time: The time when the keyframe will set.
    :parameter value: The value you want to set. 
    """
    def setValueAtTime(self, time, value):
        self.value_stack.append([time, value])

    def __str__(self):
        return str(self.default_value)

    """
    The get item attribute. Used to return an element of an array.
    
    :returns: Element of array, identified by number like normal.
    """
    def __getitem__(self, item):
        return self.default_value[int(item)]

    """
    This method checks if a value.
    
    :returns: True if the value is none else false.
    """
    def isNone(self):
        if self.default_value == None:
            return True
        else:
            return False
