'''
Exceptions in CTORs and DTORs
=============================
If is possible to raise an exception in a constructor (CTOR) or destructor (DTOR).  In the case of an exception
raised in a CTOR, they are handled just like other exceptions and no object is created.  However, if an exception
is raised in a DTOR, Python ignores the exception and prints an error message.

So the rule is, don't raise exceptions in DTORs.  And with what I said earlier about the non deterministic nature
of when a DTOR is called you are advised not to use DTORs at all in your code.
'''

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
