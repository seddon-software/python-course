'''
classmethod decorator
=====================
Python 3 introduced the classmethod decorator in which the first parameter to the method is a pointer to
the class rather than an object.  This decorator can be used to create objects within the method and hence
is often used to provide different ways of initializing the class (recall we are only allowed to provide one
__init__() method).

In this example we provide two different ways of constructing new objects:
            def initialize(theClass, x, y):
            def initialize2(theClass, a):

where the second method sets the x and y attributes to the same value.  Note that by using classmethod decorators
we don't need an __init__() and hence we've made it do nothing.
'''


class Point:
    def __init__(self): 
        pass
	
    def Print(self): 
    	print(str(self.x) + "," + str(self.y))
			
    @classmethod
    def initialize(theClass, x, y):
        p = theClass()  # Point()
        p.x = x
        p.y = y
        print(p.__dict__)
        return p
	
    @classmethod
    def initialize2(theClass, a):
    	p = theClass()
    	p.x = a
    	p.y = a
    	return p

# construct by adding attributes directly (not recommended)
p1 = Point()
p1.x = 10
p1.y = 25
p1.Print()

# construct using 2 parameters
p2 = Point.initialize(11, 26)
p2.Print()

# construct using 1 parameter
p3 = Point.initialize2(20)
p3.Print()





