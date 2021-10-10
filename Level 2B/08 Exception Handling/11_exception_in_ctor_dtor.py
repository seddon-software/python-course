############################################################
#
#    Exception in CTOR and DTOR
#
############################################################

class MyClass(object):
    # if CTOR throws, the DTOR is still called
    def __init__(self):
        raise Exception("CTOR failed")
        print("end of CTOR")
    
    # if the DTOR tries to throw, the exception is converted to a 
    # simple error message on stderr and the DTOR exits immediately 
    def __del__(self):
        raise Exception("DTOR failed")
        print("end of DTOR")


def f():
    x = MyClass()   # DTOR called after this line
    
try:
    f()
except Exception as e:
    print(e)
    
print("finished")
