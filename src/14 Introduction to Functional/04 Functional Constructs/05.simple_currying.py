'''
In this example we have 3 simple functions, each taking a time parameter.  We combine them into a more complex function using a "chain" function to combine
the curried single parameter functions.
'''

def chain(b, c, d):
	def a(x):
		return b(c(d(x)))
	return a
	
def daystohour(time):
	""" Function that converts days to hours. """
	return time * 24
	
def hourstominutes(time):
	""" Function that converts hours to minutes. """
	return time * 60
	
def minutestoseconds(time):
	""" Function that converts minutes to seconds. """
	return time * 60
	
howManySeconds = chain(minutestoseconds, hourstominutes, daystohour)
print(howManySeconds(10))
	
