from pprint import pprint

# This class factory adds each new class to a dictionary (models)
# Thus a list of all classes can be retrieved at any time
models = {}

class ModelMetaclass(type):
    def __new__(meta, name, bases, attrs):
        models[name] = cls = type.__new__(meta, name, bases, attrs)
        return cls

class Model(object, metaclass=ModelMetaclass):
    pass

class A(Model): pass
class B1(A): pass
class B2(A): pass
class B3(A): pass
class C(B1): pass

# display all the classes created with our metaclass
pprint(models)