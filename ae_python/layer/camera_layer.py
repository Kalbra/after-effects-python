from ae_python.layer.layer import Layer

class CameraLayer(Layer):
    """
    The CameraLayer object represents a camera layer within a composition.

    :parameter zoom: The zoom factor of the camera.
    :parameter center_point: The center of the new camera, a floating-point array [x, y]. This is used to set the
               initial x and y values of the new camera’s Point of Interest property. The z value is set to 0.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.zoom = kwargs.get("zoom")
        self.center_point = kwargs.get("center_point")

