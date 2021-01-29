from ae_python.ae_script import *
from ae_python.comp import *
from ae_python.layer import ShapeLayer
from ae_python.shape.rectangle_shape import Rectangle
from colour import Color

after_effects_script = AEScript()

composition = Comp(name="Shape", comment="The Shape example of ae-python")

shape_layer = ShapeLayer()

shape_layer.addShape(Rectangle(color=Color("green"), size=[200, 200], roundness=40))

after_effects_script.addComp(composition)
