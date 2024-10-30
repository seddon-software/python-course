'''
Deleter Decorator
=================

This decorator is used to prevent accidental deletion of an attribute.  Again we must also provide a
property decorator before defing the deleter decoration on the "attribute".
'''

import math

class Circle(object):
    def __init__(self, radius):
        self.theRadius = radius

    @property
    def radius(self):
        return self.theRadius
    
    @radius.deleter      # version 2.6
    def radius(self):
        raise TypeError("can't delete radius")
                
try:
    circle = Circle(10.0)
    del circle.radius
except TypeError as e:
	print(f"Error: {e}")


1
