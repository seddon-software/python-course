class A:
    x = "class attribute A"
    y = "class attribute A"
    z = "class attribute A"
    def __init__(self):
        self.x = "object attribute of class A"
        self.y = "object attribute of class A"
        self.z = "object attribute of class A"

class B(A):
    x = "class attribute B"
    y = "class attribute B"
    def __init__(self):
        A.__init__(self)
        self.x = "object attribute of class B"
        self.y = "object attribute of class B"

class C(B):
    x = "class attribute C"
    def __init__(self):
        B.__init__(self)
        self.x = "object attribute of class C"

print("dotted class lookup traverses inheritance hierarchy")
print(C.x)    
print(C.y)
print(C.z)
print()

print("dotted object lookup traverses inheritance hierarchy after object dictionary")
o = C()
print(o.x)
print(o.y)
print(o.z)
print()

print("direct dictionary lookup works the same way")
print(o.__dict__['x'])
print(o.__dict__['y'])
print(o.__dict__['z'])
    