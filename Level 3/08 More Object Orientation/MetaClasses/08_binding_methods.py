############################################################
#
#    binding
#
############################################################


# methods must be bound before they can be called
# methods can be bound to classes or objects
# binding refers to the first parameter in function call
#   with object binding the first parameter is a reference to an instance
#   with class binding the first parameter is a reference to an class
# static binding (staticmethod) works just like a function call

class A(object): 
    # methods automatically bound to object, but must have at least one parameter
    def g(self): 
        print("calling g()") # method bound to object
        print(self)
    # alternatively bind to a class
    gg = classmethod(g) # method bound to class
        
    # methods with no parameters can't be bound to an object
    # instead they must be declared as static methods (reported as functions) 
    def h(): print("calling h()")       
    h = staticmethod(h) 

# report description of functions
a = A()
print(a.g)       # bound method of object
print(a.gg)      # bound method of class
print(a.h)       # static method is reported as a function
print()

print(A.g)       # unbound when called through the class
print(A.gg)      # bound when called through the class
print(A.h)       # static method is reported as a function
print()

# call methods
a.g()
A.gg()
A.h()


1