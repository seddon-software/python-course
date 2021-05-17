############################################################
#
#    using-mro
#
############################################################

o = object
class A(o):
    def __init__(self,**kwargs):
        super(A,self).__init__()
        self.a = kwargs['a']

class B(A):
    def __init__(self,**kwargs):
        super(B,self).__init__(**kwargs)
        self.b = kwargs['b']

class C(A):
    def __init__(self,**kwargs):
        super(C,self).__init__(**kwargs)
        self.c = kwargs['c']

class D(B,C):
    def __init__(self,**kwargs):
        super(D,self).__init__(**kwargs)
        self.d = kwargs['d']

def printMRO(clazz):
    print("MRO = ", end="")
    for c in clazz.mro():
        print(c.__name__, end=" ")
    print()
        
printMRO(D)
# this will call all __init__ methods in the MRO
# but each __init__ will use the same value of self
# hence myObject.__dict__ will end up with 4 entries 
myObject = D(a=1,b=2,c=3,d=4)
print(f"myObject dict = {myObject.__dict__}")
    

