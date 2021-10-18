def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4
    
def power(fn, x):
    return fn(x)

n = int(input("enter a power: "))
print(power(lambda x:x**n, 2))
