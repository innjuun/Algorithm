# class Singleton:

#     def __new__(cls):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__new__(cls)

#         return cls._instance

# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)
# s1.a = "something"
# print(s2.a)

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

class Maker(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
logger3 = Maker()
logger4 = Maker()
print(logger1 is logger2)
print(logger2 is logger3)
print(logger3 is logger4)