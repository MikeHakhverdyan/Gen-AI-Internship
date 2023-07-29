import threading


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        lock = threading.Lock()
        with lock:
            if not cls.__instance:
                cls.__instance = object.__new__(cls, *args, **kwargs)
                return cls.__instance
        return cls.__instance

    def __new__(cls, name, bases, attrs):
        cls.__instance = None
        return super().__new__(cls, name, bases, attrs)


class TargetClass(metaclass=SingletonMeta):
    pass

target1 = TargetClass()
target2 = TargetClass()

print(target1, target2)