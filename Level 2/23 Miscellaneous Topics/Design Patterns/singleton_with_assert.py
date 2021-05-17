def singleton(object, instantiated=[]):
    "Raise an exception if an object of this class has been instantiated before."
    assert object.__class__ not in instantiated, \
        "%s is a Singleton class but is already instantiated" % object.__class__
    instantiated.append(object.__class__)

class YourClass:
    "A singleton class to do something ..."
    def __init__(self, args):
        singleton(self)


x1 = YourClass([1,2,3])
x2 = YourClass([4,5,6])

1