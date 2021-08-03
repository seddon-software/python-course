def f(x):
    y = x * x       # defines a local variable
    print(("locals for f(): ", locals()))        
    def inner():
        print(("locals for inner(): ", locals()))        
        z = y * 2   # defines a new local variable (y) which shadows that defined in f
                    # hence the RHS of this expression refers to the local y which is undefined 
        y = z
        return y
    inner()
    print(y)
    return inner()

try:
    print((f(5)))
except UnboundLocalError as e:
    print(e)
    
1
