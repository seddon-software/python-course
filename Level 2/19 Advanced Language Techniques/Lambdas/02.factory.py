############################################################
#
#    lambda functions
#
############################################################

def factory(n):
	if (n == 2):
		return lambda x,y=0 : x + y
	if (n == 3):
		return lambda z : z * z * z
	if (n == 4):
		return lambda x : x * x * x * x
		
sum = factory(2)
cube = factory(3)
quad = factory(4)

print((sum(7)))
print((sum(14,9)))
print((sum(70,30)))
print((cube(5)))
print((quad(10)))


1