'''
Property Setter Decorator
=========================

As we have seen, the property decorator creates read only access to a method.  The property getter decorator
allows read write access.  However, we must first provide a property decorator for the attribute we wish to 
modify.  We then have two ways to acces the attribute - read only and read write.

Note the atribute we work with is often not the attribute store in the object's dictionary.  For example, in
the code below it looks as though our Circle object has a "radius" attribute, but in fact it onlt has
"theRadius" attribute in it's dictionary.  This gives a primitive form of data hiding.

Note that the property getter decorator must ensure we don't put invalid values into the object's dictionary.
'''

import math

class Circle(object):
    def __init__(self, radius):
        self.theRadius = radius

    @property
    def radius(self):
        return self.theRadius
    
    @radius.setter      # version 2.6
    def radius(self, value):
        # check new value is valid
        if not isinstance(value, float):
            raise TypeError("must be a float")
        self.theRadius = value
        
circle1 = Circle(10.0)
circle2 = Circle(20.0)
circle3 = Circle(30.0)

circle1.radius = 15.0
print(circle1.radius)

# see what is actually in the object's dictionary (note: no "radius")
print(circle1.__dict__)

circle2.radius = 25.0
print(circle2.radius)

# try to something silly
try:
    circle3.radius = "big"
except TypeError as e:
    print(f"Error: radius {e}")



