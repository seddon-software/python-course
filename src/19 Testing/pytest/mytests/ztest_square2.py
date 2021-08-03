import math 
 
def doit(fn):
	def dec():
		test_2 = fn
		return test_2
	return dec
	
@doit
def xtest_sqrt(): 
 num=25 
 assert math.sqrt(num) == 5 
 
def testsquare(): 
 num=7 
 assert 7*7 == 40 
 
def tesequality(): 
 assert 10 == 11 

