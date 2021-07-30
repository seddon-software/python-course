def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4

def powers(fn, n):
    return fn(n)

print( powers(square, 5) )
print( powers(square, 7) )
print( powers(square, 9) )
print( powers(cube, 6) )
print( powers(cube, 8) )
print( powers(cube, 10) )
print( powers(quad, 13) )
print( powers(quad, 15) )
print( powers(quad, 17) )

# raising to the seventh power will only be used once
# so just use a lamda
print( powers(lambda x:x**7, 2))