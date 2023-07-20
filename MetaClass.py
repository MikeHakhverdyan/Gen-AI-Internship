# class TypeCheckMeta(type):
#     def __new__(cls, name, bases, attrs):
#         # Iterate over class attributes
#         for attr_name, attr_value in attrs.items():
#             # Check if the attribute is a type annotation
#             if hasattr(attr_value, '__origin__') and attr_value.__origin__ == type:
#                 # Get the expected type from the type annotation
#                 expected_type = attr_value.__args__[0]
#
#                 # Define a property for the attribute with type checking
#                 def property_with_type_check(expected_type):
#                     _value = None  # Store the actual attribute value
#
#                     def getter(self):
#                         return _value
#
#                     def setter(self, value):
#                         if not isinstance(value, expected_type):
#                             raise TypeError(f"Expected {expected_type.__name__} for attribute '{attr_name}', but got {type(value).__name__}")
#                         nonlocal _value
#                         _value = value
#
#                     return property(getter, setter)
#
#                 # Replace the attribute with a property that performs type checking
#                 attrs[attr_name] = property_with_type_check(expected_type)
#
#         return super().__new__(cls, name, bases, attrs)
#
# class MyClass(metaclass=TypeCheckMeta):
#     name: str
#     age: int
#
#
# obj = MyClass()
# obj.name = "John"  # Valid assignment
# obj.age = 25  # Valid assignment
#
# obj.name = 123  # Raises TypeError: Expected str for attribute 'name', but got int
# obj.age = "25"  # Raises TypeError: Expected int for attribute 'age', but got str
#
#
# print(obj.__dict__)


##########################


class TypeCheckMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr, value in attrs.items():
            if attr.startswith("__"):
                new_attrs[attr] = value
            else:
                new_attrs[attr] = cls.wrap_attribute(attr, value)
        return super().__new__(cls, name, bases, new_attrs)

    @staticmethod
    def wrap_attribute(attr, value):
        def type_checked_setter(instance, new_value):
            if not isinstance(new_value, type(value)):
                raise TypeError(f"Invalid type assigned to '{attr}'. Expected '{type(value).__name__}', got '{type(new_value).__name__}'.")
            setattr(instance, f"_{attr}", new_value)

        def type_checked_getter(instance):
            return getattr(instance, f"_{attr}")

        return property(type_checked_getter, type_checked_setter)


class MyClass(metaclass=TypeCheckMeta):
    integer_attr = 0
    float_attr = 0.0
    string_attr = ""

    def __init__(self, integer_attr, float_attr, string_attr):
        self.integer_attr = integer_attr
        self.float_attr = float_attr
        self.string_attr = string_attr


obj = MyClass(1, 31.4, "Hello, world!")
print(MyClass.__dict__)

