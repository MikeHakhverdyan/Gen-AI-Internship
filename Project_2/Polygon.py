from Point2D import Point2D
from Point2D_Sequence import Point2D_Sequence

class Polygon:
    _min = 3
    _max = 12
    _vertices = Point2D_Sequence(_min, _max)

    def __init__(self, *vertices):
        self._vertices = vertices

    def append(self, new_vertice):
        if not isinstance(new_vertice, Point2D):
            raise TypeError("New vertice must be of type Point2D.")
        if len(self._vertices) + 1 > self._max:
            raise ValueError(f"Maximum amount of verices is exceeded")

    def __str__(self):
        s = ""
        for i in self._vertices:
            s += str(i) + "\n"
        return s

p = Polygon(Point2D(0, 1), Point2D(5, 0), Point2D(6, 4))
print(p)