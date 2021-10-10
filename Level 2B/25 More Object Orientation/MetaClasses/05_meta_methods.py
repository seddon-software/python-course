class MyMetaclassA(type):
    def f1(self): print("f1() meta method")

class MyMetaclassB(MyMetaclassA):
    def f2(self): print("f2() meta method")

class MyMetaclassC(MyMetaclassB):
    def f3(self): print("f3() meta method")

class A(object, metaclass=MyMetaclassC):
    def g1(self): print("g1() class method")
    g1 = classmethod(g1)    #  convert instance to class method
    
class B(A):
    def g2(self): print("g2() class method")
    g2 = classmethod(g2)
    
class C(B):
    def g3(cls): print("g3() class method")
    g3 = classmethod(g3)
    
# invoke methods through the class
C.g3()
C.g2()
C.g1()
C.f3()
C.f2()
C.f1()

# invoke methods through an instance
try:
    o = C()
    o.g3()
    o.g2()
    o.g1()
    o.f3()  # fails; objects can't see meta classes
    o.f2()
    o.f1()
except AttributeError as e:
    print(e)

