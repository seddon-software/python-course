import sympy
sympy.init_printing()

# define symbols
x , y , z = sympy.symbols('x, y, z')

# print polynominal in two different forms 
print "1: ", 2*(x - 3)**3
print "2: ", (2*(x - 3)**3).expand()

# evaluate polynominal with a given value of x
print "3: ", ((x + 2*y)**2).subs(x, 10)

# evaluate polynominal with a given values of x and y
print "4: ", ((x + 2*y)**2).subs({x:10, y:3})

# perform double substitution on expression 
myterm = ((x + 2*y)**2)
print "5: ", myterm
print "6: ", myterm.subs(x, y).subs(y, 2)