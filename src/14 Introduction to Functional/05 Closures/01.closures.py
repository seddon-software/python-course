'''
Closures
========
Python allows nested functions as the example below.  Note that when calling the nested function "g" we don't
pass the x and y lists to "g" as parameters even though we modify x and y in "g".  This is because of closures.

The function "g" sees variables defined in its environment (or closure).  The environment "encloses" the 
surrounding scope of "g".  Python allows us to explicity see the closure with (see utils.py)
            <function>.__closure__

A closure is when an inner function retains access to its outer function's variables, even after the outer 
function has finished executing. It "remembers" the environment in which it was created, allowing it to access 
variables outside its immediate scope.

In this example, the closure has 2 items (x and y).  Note that only mutable items referenced in "g" will be
included in this closure (so variable a is not part of the closure).
'''

from utils import *     # for displayClosures

def f():
    a = [100]; print(f"a:{id(a):x}")
    x = [200]; print(f"x:{id(x):x}")
    y = [300]; print(f"y:{id(y):x}")
    def g():
        # a not referenced, so not part of closure
        x.append(201)
        y.append(301)
    g()
    displayClosures(g)

f()
