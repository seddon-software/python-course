import sympy, matplotlib
from sympy import integrate, sin, exp
sympy.init_printing()

x, y, sigma = sympy.symbols('x, y, sigma')

print integrate( x**2, x )
print integrate( x**2, y )


print integrate( sin(x), y )
print integrate( sin(x), x )
print integrate( -x * exp(-x**2/2), x )


print integrate( x**2, x, x, y )   # triple integral dx, dx, dy
print integrate( x**2, (x, 0, 2), x, y )   # triple integral dx, dx, dy
print integrate( x**2, (x, 0, 2), (x, 0, 2), y )   # triple integral dx, dx, dy
print integrate( x**2, (x, 0, 2), (x, 0, 2), (y, 0, 1) )   # triple integral dx, dx, dy
print (float) (integrate( x**2, (x, 0, 2), (x, 0, 2), (y, 0, 1) ))

#12.1.5