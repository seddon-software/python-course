from sympy import symbols, exp, sin, sqrt, diff
x, y = symbols('x, y')

# various differentials

print diff( sin(x), x )
print diff( 10 + 3*x + 4*y + 10*x**2 + x**9, x)
print diff( 10 + 3*x + 4*y + 10*x**2 + x**9, x).subs(x, 1.5)

print diff( exp(x), x )
print diff( exp(-x**2 / 2), x )
print diff(3*x**4, x)

# now for triple differentials
print diff(3*x**4, x, x, x) # d3y/dx3
print diff(3*x**4, x, 3)    # the same
import sympy
for key in sympy.__dict__:
    print key