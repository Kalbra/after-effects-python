from ae_python.layer.layer import Layer
from ae_python.property import Property

class CameraLayer(Layer):
    """
    The Camera layer object represents a camera layer within a composition.

    :parameter zoom: The zoom factor of the camera.
    :parameter center_point: The center of the new camera, a floating-point array [x, y]. This is used to set the
               initial x and y values of the new camera’s Point of Interest property. The z value is set to 0.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.properties.append(["zoom", Property(kwargs.get("zoom"))])
        self.properties.append(["center_point", Property(kwargs.get("center_point"))])

