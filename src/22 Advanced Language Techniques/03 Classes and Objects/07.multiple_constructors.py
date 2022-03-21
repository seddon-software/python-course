'''
Multiple Contructors
====================
Unlike many othe languages, Python doesn't permit overloading __init__ to allow for multiple constructors.
However you can use __new__ to simulate multiple constructors as shown below.  

Note that the different constructors all have to have different names and because __init__ is always called 
after __new__, don't define __init__ for your class and just let the default "do nothing" version called instead.
'''

class A:
    def __new__(clazz, *args):
        obj = object.__new__(clazz)
        
        if len(args) == 1: 
            if type(args[0]) is type(str()):
                A.__init__ = A.CTOR3
            elif type(args[0]) is type(int()):
                A.__init__ = A.CTOR1
        if len(args) == 2: 
            A.__init__ = A.CTOR2 
        return obj
    
    def CTOR1(self, x):
        print("CTOR1 called")
        self.x = x
        
    def CTOR2(self, x, y):
        print("CTOR2 called")
        self.x = x
        self.y = y
        
    def CTOR3(self, s):
        print("CTOR3 called")
        self.x, self.y = [int(i) for i in s.split(" ")]


try:
    a1 = A(42)          # call CTOR1
    a2 = A(42, 52)      # call CTOR2
    a3 = A("5 12")      # call CTOR3
except Exception as error:
    print(error)




