import math

class Circle(object):
    def __init__(self, radius):
        self.theRadius = radius

    @property
    def radius(self):
        return self.theRadius
    
    @radius.setter      # version 2.6
    def radius(self, value):
        if not isinstance(value, float):
            raise TypeError("Must be a float")
        self.theRadius = value
        
circle1 = Circle(10.0)
circle2 = Circle(20.0)
circle3 = Circle(30.0)
print(circle1.__dict__)
circle1.radius = 15.0
print(circle1.radius)

circle2.radius = 25.0
print(circle2.radius)

try:
    circle3.radius = "big"
except TypeError as e:
    print(e)


1
