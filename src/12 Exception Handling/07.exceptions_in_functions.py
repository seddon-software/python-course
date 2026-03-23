'''
Exceptions in Functions
=======================
Inside a try block, if you make a call to another function then the code inside that function is considered as
being inside the try block.

Here "f1()" is called from the try block and then "f1()" calls "f2()" and then "f3()" is called.  An exception
is raised in "f3()".  Because exception handling is a "GOTO" technology, the remaining code in each of these 
functions is never executed:
            print("Leaving f1")
            print("Leaving f2")
            print("Leaving f3")


Note that each function created a local instance of an A class.  These objects will all get deallocated by the
Python runtime.  This means their destructors (the opposite of a constructor) get called automatically.

Note that the destructors actually get called by the garbage collector.  With CPython the destructors tend to
get called immediately.  However, this is not guaranteed.  Indeed other Python interpreters may behave 
differently and their garbage collectors may delay calling the destuctors.  It may happen that the program ends 
before the garbage collector has a chance to call the destructors.  For all of these reasons it not wise to rely 
on executing code inside a destructor; better to use "finally" blocks or "with" statements.
'''

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

