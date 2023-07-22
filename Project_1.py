class ValidType:
    def __init__(self, data_type):
        self.data_type = data_type

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise ValueError(f'{self.name} must be a {self.data_type}.')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        getattr(instance, self.name)

class Int(ValidType):
    def __init__(self):
        super().__init__(int)

class Float(ValidType):
    def __init__(self):
        super().__init__(float)

class List(ValidType):
    def __init__(self):
        super().__init__(list)

class Person:
    name = ValidType(str)
    age = Int()
    height = Int()
    tags = List()
    favourite_foods = List()

    def __init__(self, name, age, height, tags, favourite_foods):
        self.name = name
        self.age = age
        self.height = height
        self.tags = tags
        self.favourite_foods = favourite_foods

p1 = Person('Josh', 15, 175, ['sport', 'music'], ['lazania', 'chamichov plav'])