from SlottedStruct import SlottedStruct

class Point4D(metaclass=SlottedStruct):
    __slots__ = ("_x", "_y", "_z", "_w")

    def __init__(self, x, y, z, w):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def w(self):
        return self._w
