############################################################
#
#    decorators
#
############################################################

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
print(quad(10))
# here is what is actually happening with the decorator
def square2(x): 
    return x * x
print(trace(square2)(4))
