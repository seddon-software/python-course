############################################################
#
#    decorators
#
############################################################


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
    
print(square(4))
print(cube(5))

trace.disable()
print(quad(10))

trace.enable()
print(square(6))
print(cube(7))


