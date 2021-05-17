############################################################
#
#    explict object creation using __new__ 
#
############################################################


class A:
    def __new__(clazz, arg):        # implicitly static
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



1
