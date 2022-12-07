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

############################################################
# Part 1 - no closure (immutable l-value)
def outer():
    x = 50      # local variable, lifetime ends at end of function
    def inner():
        x += 1  # x refers to local x, not a closure on outer.x so this raises an exception
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

def outer():
    x = [50]     # x is mutable and will be part of the closure
    def inner():
        print(f"closure on outer, x = {inner.__closure__[1].cell_contents}")
        x[0] += 1  # x refers to outer 'x' because its mutable => closure
        print(f"closure on outer, x = {inner.__closure__[1].cell_contents}")
    return inner

f = outer()
try:
    f()     # outer 'x' is brought into scope by the closure
            # hence NO exception raised
except UnboundLocalError as e:
    print(e)
