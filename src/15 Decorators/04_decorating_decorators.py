'''
Decorating Decorators
=====================

You can even decorate decorators!  

Here we return to out "trace()" decorator example.  The "toggleable()" decorator is used to switch the "trace()" 
decorator on and off.  This decorator takes a parameter and as with the "logging()" decorator it is defined as
3 levels of nested functions.  Note that there are 2 further nested functions.
            def enable()
            def disable()

This time the translated code is a little more complex.

Before we continue, note the toggleable decorator adds 2 attributes to the enhance function object such that
            enhance.enable = toggleable.enable
            enhance.disable = toggleable.disable            


1. Now a call to
            trace.enable()
gets translated to
            toggleable(trace).enable() with closure on decorator=trace
and toggleable(trace) returns enhance, so the above is equivalent to 
            enhance.enable()
and because the enhance.enable = toggleable.enable, this then calls "toggleable.enable()" with decorator = trace
and we end up with
            decorator.enable = True
or
            trace.enable = True

2. Next the call
            square(4)
gets translated (because square is decorated) to 
            trace(square)(4)
which further translates (because trace is decorated) to
            toggleable(trace)(square)(4)
and this contracts to (toggleable(trace) returns enhance):
            enhance(square)(4)
and then (enhance(square) returns inner): 
            inner(4) with closure: decorator = trace, fn = square, x = 4
and since trace.enabled is True, inner returns
            decorator(fn)(x)
or
            trace(square)(4)
'''


def toggleable(decorator):
    def enhance(fn):
        def inner(x):
            if decorator.enabled:
                return decorator(fn)(x)
            else:
                return fn(x)
        return inner
    def enable():
        decorator.enabled = True
    def disable():
        decorator.enabled = False
    enhance.enable = enable
    enhance.disable = disable
    enable()
    return enhance

@toggleable
def trace(fn):
    def enhance(x):
        print("calling {}({})".format(fn.__name__, x))
        return fn(x)
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

trace.enable()    
print(square(4))
print(cube(5))

trace.disable()
print(quad(10))

trace.enable()
print(square(6))
print(cube(7))


