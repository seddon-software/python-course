'''
Gotchas
========

Recall the closures will be on mutable variables and r-valued immutable variables.  In this gotcha we are
trying to use y from the "outer" function in "inner".  The code looks OK, but the lines
        z = y * 2
        y = z
actually define a new local variable "y".  This is because y is used an an l-value (left hand side of =) on the 
second line.  The second line now refers to the local y which is so far undefined and hence the line raises an 
exception.

Thus the code fails.
'''

def f(x):
    y = x * x       # defines a local variable y
    print("locals for f(): ", locals())       
    def inner():
        print(f"locals for inner(): {locals()}")        
        try:
            z = y * 2   # the RHS of this expression refers to the local y which is undefined at present
                        # and not a closure on the outer y 
        except UnboundLocalError as e:
            print(e)
        y = 99       # attempts to define a new local variable y (immutable l-value)
        print(f"locals for inner(): {locals()}")        
        return y
    result = inner()
    return result       # propogate the result to global scope

print(f(5))
    

