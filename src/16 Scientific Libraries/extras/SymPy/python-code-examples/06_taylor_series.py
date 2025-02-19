from sympy import Symbol, Rational, cos, sin, series

x = Symbol('x') 
print(cos(x).series(x, 0.5, 10))
print(cos(x).series(x, 0.5, 10).removeO())
from sympy.series import series
print(series(cos(x), x0=Rational(0.5), n=10))
print(series(cos(x), x0=0, n=10))
