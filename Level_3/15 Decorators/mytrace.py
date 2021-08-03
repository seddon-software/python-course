def trace(fn):
    def enhance(z):
        print(f"calling {fn.__name__}({z})")
        return fn(z)
    return enhance

@trace
def square(n):
    return n**2

@trace
def cube(n):
    return n**3

@trace
def quad(n):
    return n**4

x = square(7)  # x = trace(square)(7)
print(x)


