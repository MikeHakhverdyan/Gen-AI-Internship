class SlottedStruct(type):
    def __init__(cls, name, bases, attrs):
        if '__slots__' not in attrs:
            raise TypeError('Class must be defined with __slots__ attribute')
        type.__init__(cls, name, bases, attrs)

    def __eq__(cls, other):
        if not isinstance(other, cls):
            return False
        return all(getattr(cls, slot) == getattr(other, slot) for slot in cls.__slots__)

    def __hash__(cls):
        return hash(tuple(getattr(cls, slot) for slot in cls.__slots__))

    def __str__(cls):
        return f"({', '.join(str(getattr(cls, slot)) for slot in cls.__slots__)})"
