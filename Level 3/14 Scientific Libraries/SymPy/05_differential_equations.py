from sympy import Symbol
import sympy

x , y , z = sympy.symbols('x, y, z')

from sympy import Symbol , dsolve , Function , Derivative , Eq
y = Function("y")
x = Symbol("x")
dy_dx = Derivative(y(x), x)
'''
dy/dx + 5y = 0 (find y)   => dy/y = -5dx 
                          => ln y = -5x + C 
                          => y = exp(-5x + C) 
                          => y = C1*exp(-5x)
'''
print dsolve(dy_dx + 5*y(x), y(x))
print dsolve( Eq(dy_dx + 5*y(x), 0), y(x)) # more verbose
print dsolve( Eq(dy_dx + 5*y(x), 12), y(x)) # dy/dx + 5y = 12
C1 = Symbol("C1")
print dsolve( Eq(dy_dx + 5*y(x), 12), y(x)).subs({C1:2, x:5}) # dy/dx + 5y = 12
print dsolve( Eq(dy_dx + 5*y(x), 12), y(x)).subs({C1:2, x:5}).evalf(20) # dy/dx + 5y = 12
