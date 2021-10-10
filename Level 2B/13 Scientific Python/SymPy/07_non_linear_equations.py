import sympy
import pylab as plt

x, y, z = sympy.symbols('x, y, z')
eq = x - x**2.5 + 7
z = sympy.solve( eq, x )
 
# note most of the results are complex (I represents sqrt(-1))
for result in z:
    print(sympy.N(result, 5))    # N is used to limit precision

plt.gca().set_title('Y = X - X**2.5 + 7')

# show the graph
X = (1 + 0j) * plt.arange(-5, 5, 0.1)
Y = X - X**2.5 + 7
plt.plot(X.real, Y.real, color='red', lw=2, label='real')
plt.plot(X.real, Y.imag, color='green', lw=2, label='imag')
plt.legend()

X = plt.arange(-5, 5, 0.1)
plt.grid()
plt.show()
