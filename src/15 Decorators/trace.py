def trace(fn):
    def enhance(n):
        # decorator part
        print(f"calling {fn.__name__}({n})")
        # call original function
        return fn(n)
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

# x = trace(quad)(10)
x = quad(10)
print(x)


    
    