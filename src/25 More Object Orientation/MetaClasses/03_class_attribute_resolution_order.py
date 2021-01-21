# This example shows how attributes are resolved for classes

class MyMetaclassA(type):
    x1 = 1

class MyMetaclassB(MyMetaclassA):
    x2 = 2

class MyMetaclassC(MyMetaclassB):
    x3 = 3

class A(object, metaclass=MyMetaclassC):
    y1 = 11
    
class B(A):
    y2 = 22
    
class C(B):
    y3 = 33
    
# working with classes
# lookup chain for attributes starts with the class, 
# then each class in inheritance tree using method resolution order (MRO)
# then each metaclass in its inheritance tree using MRO

print(MyMetaclassC.__mro__)
print(C.mro())
print(C.y3)
print(C.y2)
print(C.y1)
print(C.x3)
print(C.x2)
print(C.x1)

# working with objects
# lookup chain for attributes starts with the object, 
# then each class in inheritance tree using method resolution order (MRO)
# but NOT each metaclass in its inheritance tree using MRO

o = C()
o.z = 111

try:
    print(o.z)
    print(o.y3)
    print(o.y2)
    print(o.y1)
    print(o.x3)  # fails
    print(o.x2)  # fails
    print(o.x1)  # fails
except AttributeError as e:
    print(e)

