'''

Decorators take a function pointer as a parameter; this is the function being decorated.  The decorator follows 
a familiar pattern: define a nested function and then return a pointer to this function.  Normally the nested 
function will call the original function (but it doesn't have to).

When we call a decorated function as in:
            square(4)

the interpreter modifies the code to
            trace(square)(4)
and this reduces to (since trace(square) returns enhance):
            enhance(4)
which prints a trace message and calls
            square(4)

Notice that the "enhance()" function has access to the parameter passed to the decorator (fn) by closure.

So in summary, when a function "fn" is decorated with a decorator "d":
            @trace
            def fn(x): ...
calls to "fn" get replaced with:
            fn(x)  --> trace(fn)(x)
'''

def trace(fn):
    def enhance(x):
        print(f"calling {fn.__name__}{x}")
        return fn(x)        # call the function being decorated
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
    
print(square(4))
print(cube(5))
print(quad(10))
# here is what is actually happening with the decorator
def square2(x): 
    return x * x
print(trace(square2)(4))
