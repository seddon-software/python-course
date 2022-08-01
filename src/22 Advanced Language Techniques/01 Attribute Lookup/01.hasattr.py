'''
Has Attribute
=============

The hasattr is a useful builtin.  As the name implies, the function checks and object to see if it has a given
method.  
'''

class MyImplemention:
    def f1(self): print("this is f1()")
    def f3(self): print("this is f3()")

x = MyImplemention()

if hasattr(x, "f1"): x.f1()
if hasattr(x, "f2"): x.f2()
if hasattr(x, "f3"): x.f3()

