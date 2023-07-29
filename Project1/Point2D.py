from SlottedStruct import SlottedStruct

class Point2D(metaclass=SlottedStruct):
    __slots__ = ("_x", "_y")

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return SlottedStruct.__str__(self)