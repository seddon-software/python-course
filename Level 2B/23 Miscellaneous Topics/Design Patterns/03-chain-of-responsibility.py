############################################################
#
#    handling undefined attributes
#
############################################################

# Chain of Responsibility Pattern

class A(object):
    def setParent(self, parent):
        self.parent = parent

    def __getattr__(self, method):
        return getattr(self.parent, method)
    
    def f(self): print("f() found in A")
    
class B(object):
    def setParent(self, parent):
        self.parent = parent
        
    def __getattr__(self, method):
        return getattr(self.parent, method)

    def g(self): print("g() found in B")
    
class C(object):
    def setParent(self, parent):
        self.parent = parent
        
    def __getattr__(self, method):
        print("'{0}' not found in A, B or C".format(method))
        return self.doNothing   # must return something or raise an exception
    
    def h(self): print("h() found in C")
    def doNothing(self): pass
    
# use __getattr__ to implement the Chain of Responsibility pattern
a = A()
b = B()
c = C()
# link the chain
a.setParent(b)
b.setParent(c)

a.f()
a.g()
a.h()
a.dummy()

1