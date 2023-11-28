def trace(fn):
    # create a new function object
    def enhance(n):
        print(f"calling {fn.__name__}({n})")
        return fn(n)
    # return new function object
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

# print( trace(quad)(10) )
print( quad(10) )

