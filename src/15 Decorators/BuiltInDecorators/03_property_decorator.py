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
print(circle1.area)
print(circle1.perimeter)
print()

print(circle2.radius)
print(circle2.area)
print(circle2.perimeter)
print()

print(circle3.radius)
print(circle3.area)
print(circle3.perimeter)
print()


1
