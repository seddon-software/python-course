# This example defines a custom class factory that defines:
#     y, __init__(), __new__()
# The class factory is used to create other classes
# New classes use the class factory 'type', unless the metaclass
#     attribute is defined to select a different class factory

class MyClassFactory(type):
    y = 100
    def __init__(cls, name, bases, dct):
        bases = (object,)
        super(MyClassFactory, cls).__init__(name, bases, dct)
        
    def __new__(cls, name, bases, dct):
        print("Allocating memory for class", name)
        dct['y'] = MyClassFactory.y              # attribute created
        dct['f'] = lambda self: self.x + self.y; # method created
        # use the 'type' class factory type to allocate
        return type.__new__(cls, name, bases, dct)
 
class A(metaclass=MyClassFactory):
    x = 44
    # this class will also get 'y' and 'f' defined by the class factory
    
# this uses the class factory of its superclass
class B(A):
    def h(self): print(self.x)

def main():
    # investigate classes
    print("A:", dictionary(A))
    print("B:", dictionary(B))
    print("A bases: ", A.__bases__)
    print("B bases: ", B.__bases__)

    # investigate objects
    a1 = A()
    a1.p = 100
    a1.q = 200
    a2 = A()
    a2.r = 300
    b = B()
    print("a1:", dictionary(a1))
    print("a2:", dictionary(a2))    
    print("b:", dictionary(b))
    
    print("calling methods on b ...")
    b.h()
    print(b.f())
    
# helper to display relevant parts of dictionary
def dictionary(class_):
    # remove all __ entries
    d = {}
    for key, value in class_.__dict__.items():
        if not key.startswith("__"):
            d[key] = value
    return d

main()
