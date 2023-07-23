from Point2D import Point2D
from collections.abc import Sequence

class Point2D_Sequence:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, Sequence):
            return TypeError(f'{self.__class__.__name__} object should have a type of a Sequence')
        if len(value) < self.min_length:
            raise ValueError('Minimal length is not Satisfied')
        if len(value) > self.max_length:
            raise ValueError('Maximal length is exceeded')

        for item in value:
            if not isinstance(item, Point2D):
                raise TypeError('Coordinates must be Point2D type')

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
