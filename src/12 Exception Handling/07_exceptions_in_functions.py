############################################################
#
#    Nested Exceptions
#
############################################################

class A:
    def __init__(self):
        print("CTOR")
        
    def __del__(self):
        print("DTOR")
        
def f1():
    a1 = A()
    print("Entering f1")
    f2()
    print("Leaving f1")

def f2():
    a2 = A()
    print("Entering f2")
    f3()
    print("Leaving f2")
    
def f3():
    a3 = A()
    print("Entering f3")
    raise Exception("Some exception")
    print("Leaving f3")
    
        
try:
    f1()
except Exception as e:
    print(e)

print("End of program")

