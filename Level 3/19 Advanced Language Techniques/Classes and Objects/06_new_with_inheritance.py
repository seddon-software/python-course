# import math
# class A(object): 
#     def __new__(cls): 
#          a=input("enter the number")
#          b=input("enter the number")
#          c=int(a)+int(b)
#          print(c)
          
#          return super(A, cls).__new__(cls) 
   
# A()

############################################################
#
#    explict object creation using __new__ 
#
############################################################

# __new__ is called before __init__ when creating objects
class B:
    def __init__(self):
        print("B.__init__() called")

class A(B):
    def __new__(clazz, arg):        # clazz = A
        # only create objects with non negative x attribute
        if arg < 0:
            raise Exception("negative args not allowed")
        # return object.__new__(clazz)
        return super(A, clazz).__new__(clazz) 
    
    def __init__(self, arg):
        B.__init__(self)
        self.x = arg


try:
    a1 = A(42)   # calls class method __new__ and then __init__
    a2 = A(-42)
except Exception as error:
    print(error)




