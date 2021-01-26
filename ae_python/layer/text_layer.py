from ae_python.layer.layer import Layer
from ae_python.standalone_functions import hash_maker
from colour import Color


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

        self.text: str = kwargs.get("text", "Hello World!")
        self.font_family: float = kwargs.get("font_family", "Arial")
        self.font_size: int = kwargs.get("font_size", 14)
        self.font_color: Color = kwargs.get("font_color", Color("black"))

        # The text document variable name. Need for the compiler.
        self.js_text_variable_name = hash_maker()