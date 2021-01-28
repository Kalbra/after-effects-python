from typing import List

class Shape:
    """

    :parameter vertices: [ [ [point] [in] [out] ] ]
    """
    def __init__(self, point: List[List[List[int]]]):
        self.vertices     = point[0]
        self.in_tangents  = point[1]
        self.out_tangents = point[2]

    """
    Add a point at the end to a shape. 
    
    :parameter point: A int array of two items in the following style 
                      [[point_x, point_y],[t_in_x, t_in_y],[t_out_x, t_out_y]].
    """
    def addPoint(self, point):
        self.vertices.append(point[0])

        # Tries to add the tangents if the tangents not set the value is 0.
        try:
            self.in_tangents.append(point[1])
            self.out_tangents.append(point[2])

        except IndexError:
            self.in_tangents.append([0, 0])
            self.out_tangents.append([0, 0])

    """
    Deletes a vertex form the shape by index.
    
    :parameter index: The index number you want to delete.
    """
    def deletePoint(self, index: int):
        self.vertices.pop(index)
        self.in_tangents.pop(index)
        self.out_tangents.pop(index)