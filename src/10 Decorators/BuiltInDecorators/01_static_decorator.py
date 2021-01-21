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

for x in range(50): MyClass.hit()

MyClass.PrintHits()



1
