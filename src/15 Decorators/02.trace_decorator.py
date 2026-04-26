'''
This is the same example as before, except we generalise things by assuming the decorated function has variadic parameters.  We can handle 
this by defining the enhance function as:
            def enhance(*args, **kwargs):
'''

def trace(fn):
    def enhance(*args, **kwargs):
        positional = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        named = ", ".join(f"{v}" for v in args)
        print(f"calling {fn.__name__}({named}{positional})")
        return fn(*args, **kwargs)        # call the function being decorated
    return enhance
    

@trace
def square(x): 
    return x * x

@trace
def cube(x):
    return x * x * x
    
@trace
def quad(x):
    return x * x * x * x

# call by position
print(square(x=4))
print(cube(x=5))
print(quad(x=10))

# call by name
print(square(4))
print(cube(5))
print(quad(10))

