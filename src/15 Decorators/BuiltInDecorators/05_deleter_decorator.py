import math

class Circle(object):
    def __init__(self, radius):
        self.theRadius = radius

    @property
    def radius(self):
        return self.theRadius
    
    @radius.deleter      # version 2.6
    def radius(self):
        raise TypeError("Can't delete radius")
                
try:
    circle = Circle(10.0)
    del circle.radius
except TypeError as e:
	print(e)


1
