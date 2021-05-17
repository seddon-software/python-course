from sympy import *
import sympy
a, b = sympy.symbols('a, b')

# print 0.7 as a fraction 
a = Rational(7, 10)
print a

# print an expression as a fraction 
b = Rational (45 , 67)
print a * b
print a + b

# print same data as a float
print (float)(a + b)
print (a + b).evalf(27) # 27 decimal places
