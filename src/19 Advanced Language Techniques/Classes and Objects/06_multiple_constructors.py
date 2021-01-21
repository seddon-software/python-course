############################################################
#
#    explict object creation using __new__ 
#
############################################################


class A:
    def __new__(clazz, *args):
        obj = object.__new__(clazz)
        
        if len(args) == 1: 
            if type(args[0]) is type(str()):
                A.__init__ = A.ctor3
            elif type(args[0]) is type(int()):
                A.__init__ = A.ctor1
        if len(args) == 2: 
            A.__init__ = A.ctor2 
        return obj
    
    def ctor1(self, x):
        self.x = x
        
    def ctor2(self, x, y):
        self.x = x
        self.y = y
        
    def ctor3(self, s):
        self.x, self.y = [int(i) for i in s.split(" ")]


try:
    a1 = A(42)
    a2 = A(42, 52)
    a3 = A("5 12")
except Exception as error:
    print(error)



1
