'''
Property Decorator
==================

The property decorator is used to disguise a method call as an attribute assignment.  In this example the
"area" and "perimeter" methods are decorated such that they can be invoked by attribute access:
            circle1.area
            circle1.perimeter

Although the above look as though they are creating attributes in the object's dictionary, this is not the case.
Only the "radius" ends up in the object's dictionary.  The other statements get converted to method calls by the 
decorator.  Thus
            circle1.area
gets converted to 
            circle.area()
and similarly with "perimeter".  The idea is to simplify using an object for programmers who are unsure about
methods (they are happy with attribute access) and also we don't have to store the "area" and "perimeter" values
in the object's dictionary; they are computed again each time they are required.

A consequence of using the "property" decorator is that the access is always read only.
'''

import math

class Circle(object):
	def __init__(self, radius):
		self.radius = radius

	# computed properties (and hence read only)
	@property
	def area(self):
	   return math.pi*self.radius**2
	
	@property
	def perimeter(self):
	   return 2*math.pi*self.radius

circle1 = Circle(10.0)
circle2 = Circle(20.0)
circle3 = Circle(30.0)

print(circle1.__dict__)
print(circle1.radius)
print(circle1.area)         # this calls circle1.area()
print(circle1.perimeter)    # this calls circle1.perimeter()
print()

print(circle2.radius)
print(circle2.area)
print(circle2.perimeter)
print()

print(circle3.radius)
print(circle3.area)
print(circle3.perimeter)
print()

try:
    # property decorator makes access read only
    circle1.area = 40.0
except Exception as e:
    print(e)
