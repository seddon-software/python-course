'''
Decorating a Class
==================

            a = A()
gets translated to
            trace(A)()

Now trace returns "inner()" with closure on clazz = A.  Calling inner() will print the message:
            -- decorator code in here -- 
and then return "clazz" (and clazz == A).  Thus
            trace(A)() == inner()() == clazz()  == A()

Thus,
            a = A()            
performs the decorated part (in this case printing a message) and then instantiates an "A" object.  Now we have
an object, the rest of the code is standard stuff.
'''

def trace(clazz):
    def inner():
        print("-- decorator code in here --")
        return clazz()
    return inner

@trace
class A:
    def __init__(self):
        print("A.__init__() called")
    def f1(self):
        print('f1() called')
    def f2(self):
        print('f2() called')
    def f3(self):
        print('f3() called')
    def f4(self):
        print('f4() called')

a = A() # a = trace(A)()
a.f1()
a.f2()
a.f3()
a.f4()
