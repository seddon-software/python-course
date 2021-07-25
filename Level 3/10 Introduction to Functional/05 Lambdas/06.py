def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4

def powers(fn, n):
    return fn(n)

print( powers(square, 5) )
print( powers(cube, 6) )
print( powers(quad, 10) )
print( powers(lambda x:x**7, 2))