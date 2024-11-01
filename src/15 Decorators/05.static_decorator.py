'''
Static Decorator
================

In Python 2, every method of a class had to have "self" as its first parameter.  This caused problems with
class methods (aka static methods) where we operate on an attribute that's shared between all objects.  In such
cases there is no "self" object, so the method should not have such a parameter.  To overcome this difficiency 
the @static decorator was introduced.

In Python 3, this decorator is no longer required, but still works and is often used to highlight such methods.
In this example we record the number of times the hit() method is called.  This method can be called directly through the
class as in:
            MyClass.hit()

or through an object as in:
            m1.hit()
'''

class MyClass:
	# static data
	hits = 0
	
	@staticmethod
	def hit():
		MyClass.hits = MyClass.hits + 1

	@staticmethod
	def PrintHits():
		print("hits = " + str(MyClass.hits))

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

# call static method
for x in range(50): 
    MyClass.hit()
    m1.hit()
    m2.hit()
    m3.hit()
    
# print number of hits
MyClass.PrintHits()



1
