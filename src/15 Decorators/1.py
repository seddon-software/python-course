def trace(fn):
    def enhance(n):  # enhance = F.O.
        print(f"calling {fn.__name__}({n})")
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

# print( trace(square)(5) ) 
# print( trace(cube)(7) )
# print( trace(quad)(10) )
print( square(5) ) 
print( cube(7) )
print( quad(10) )
