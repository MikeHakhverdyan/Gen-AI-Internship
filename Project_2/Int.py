class Int:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('The type of a value must be an Integer')
        if value < 0:
            raise ValueError('Value must be non negative')
        if value > self.max_value or value < self.min_value:
            raise ValueError(f'The value must be in ({self.min_value} ; {self.max_value}) range')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)
