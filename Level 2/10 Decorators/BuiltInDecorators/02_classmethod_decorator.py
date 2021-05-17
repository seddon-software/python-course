class Point:
	def __init__(self): 
		pass
	
	def Print(self): 
		print(str(self.x) + "," + str(self.y))
			
	@classmethod
	def initialize(theClass, x, y):
		p = theClass()
		p.x = x
		p.y = y
		return p
	
	@classmethod
	def initialize2(theClass, a):
		p = theClass()
		p.x = a
		p.y = a
		return p

p1 = Point()
p1.x = 10
p1.y = 25
p1.Print()

p2 = Point.initialize(11, 26)
p2.Print()

p3 = Point.initialize2(20)
p3.Print()


1


