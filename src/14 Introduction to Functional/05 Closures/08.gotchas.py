'''
Gotchas
=======

Referring to the previous example which raised an exception, one workaround is to make x mutable.  Here is
a slightly different example illustrating the point.  

In part 1, the outer function returns a pointer to the inner function.  The inner function tries to increment x,
but since
            x += 1
is really
            x = x + 1
we are incrementing by an int and hence x will have type int.  This means x is immutable which in turn means it
will be defined as a local variable. Now the right hand side of this line also refers to x.  Which x?  Is it the
outer x because of a closure or is it the local x defined on the left hand side of the line?

Local variables always take preference over closures, so x is referring to the local x.  Trouble is the local
x hasn't yet been assigned (unbound local) and hence an exception is raised.

In part 2 we store 50 in a list.  Since the list is mutable, it is captured by the closure and can be modified 
without raising an exception.
'''

import os
os.system("clear")

############################################################
# Part 1 - no closure (immutable l-value)
def outer():
    x = 50      # immutable local variable, lifetime ends at end of function
    def inner():
        try:
                    # x appears on LHS of assignment, hence ...
            x += 1  # x refers to local x, not a closure on outer.x so this raises an exception
        except Exception as e:
            print(e)
    return inner

f = outer()
try:
    f()     # outer 'x' is not in scope here (outer has already returned)
            # hence exception raised
except UnboundLocalError as e:
    print(e)

print()

############################################################
# Part 2 - workaround for the above problem

def displayClosures(fn):
    if fn.__closure__:
        closures = zip(fn.__closure__, fn.__code__.co_freevars)
        next(closures)      # skip the closure cell on the function name (always the first)
        for c, f in closures:
            print(f"closure for {fn.__name__}: {f} = {c.cell_contents}")
    else:
        print(f"closure for {fn.__name__}: empty")

def outer():
    x = [50]     # x is mutable and will be part of the closure
    def inner():
        displayClosures(inner)
#        print(f"closure on outer, x = {inner.__closure__[1].cell_contents}")
        x[0] += 1  # x refers to outer 'x' because its mutable => closure
        displayClosures(inner)
#        print(f"closure on outer, x = {inner.__closure__[1].cell_contents}")
    return inner

f = outer()
try:
    f()     # outer 'x' is brought into scope by the closure
            # hence NO exception raised
except UnboundLocalError as e:
    print(e)
