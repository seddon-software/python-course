# The function partial of the module functools of Python allows you to create partially applied functions. A partially applied function is a new function that is derived from an existing function by fixing a certain number of arguments in advance. The result is a function that can be called with the remaining arguments. We can use it for the commposition of functions.



# Demonstrate Currying of composition of function

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
	
if __name__ == '__main__':
	transform = chain(minutestoseconds, hourstominutes, daystohour)
	e = transform(10)
	print(e)
	
