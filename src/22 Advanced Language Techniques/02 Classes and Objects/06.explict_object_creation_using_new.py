'''
Explict Object Creation using __new__
===================================== 
When an object is created, Python arranges for special methods to be called.  It is well known that "__init__()" 
is called to initialise the object, but did you know "__new__()" is called before that to allocate memory for the
object.  Normally you will allow Python to allocate memory for your objects, but you have the option of
changing how memory is allocated by using "__new__()" and which addition methods you want to call before __init__(). 

Because __new__() is called before the object is created it doesn't have a "self" parameter.  However it does have 
a pointer to the class (but you can't call it class as that's a reserved word - I've called it clazz).

In this artificial example I've used "__new__()" to prohibit objects with a negative "x" attribute by raising an
exception.  Note that
for objects you do want, you can call 
            object.__new__(clazz)
to allocate memory and avoid a recursive call.  

Other things you can do in "__new__()" include limiting the number of objects created (e.g singleton) or calling
other constructors.
'''

class A:
    # __new__ is called before __init__ when creating objects
    def __new__(clazz, arg):        # clazz = A
        # only create objects with non negative x attribute
        if arg < 0:
            raise Exception("negative args not allowed")
        return object.__new__(clazz)
    
    def __init__(self, arg):
        self.x = arg


try:
    a1 = A(42)   # calls static method __new__ and then __init__
    a2 = A(-42)
except Exception as error:
    print(error)




