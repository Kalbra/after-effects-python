from ae_python.layer.layer import Layer
from ae_python.standalone_functions import hash_maker
from colour import Color
from ae_python.property import Property

class TextLayer(Layer):
    """
    The TextLayer object represents a text layer within a composition.

    :parameter text: The text of the text layer.
    :parameter font_family: The font family of the text.
    :ref:`anchor text <https://www.adobe.com/content/dam/acom/en/fontfolio/pdfs/fontfolio11.1_font_list.pdf>`
    :parameter font_size: The font size of the text. The unit is px. Note: The value is float.
    :parameter font_color: The text color, the argument class is Color.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.properties.append(["text", Property(kwargs.get("text", "Hello World!"))])
        self.properties.append(["font_family", Property(kwargs.get("font_family", "Arial"))])
        self.properties.append(["font_size", Property(kwargs.get("font_size", 14))])
        self.properties.append(["font_color", Property(kwargs.get("font_color", Color("white")))])

        # The text document variable name. Need for the compiler.
        self.js_text_variable_name = hash_maker()