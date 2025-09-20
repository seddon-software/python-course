'''
Gotchas
=======

Here an outer function returns a pointer to the inner function.  The inner function tries to increment x,
which is declared in the outer function with:
            x += 1
which is really
            x = x + 1

x has type int and is immutable which in turn means it will be defined as a local variable in outer. 
When we try to assign to x in the inner function it is not a closure (because of the immutability) and hence
gets defined as a new local in the inner function.  However, this local x hasn't yet been assigned (unbound local) 
and hence an exception is raised.

In part 2 we store 50 in a list.  Since the list is mutable, it is captured by the closure and can be modified 
without raising an exception.

In part 3 we use the nonlocal keyword which allows the inner function to modify the outer function's x without
creating a local variable in inner.
'''

from utils import *     # for displayClosures


############################################################
# Part 1 - no closure (immutable l-value)
def part1():
    def outer():
        x = 50      # immutable local variable, not a closure
        def inner():
            try:
                        # x appears on LHS of assignment, hence ...
                x += 1  # x refers to local x, so this raises an exception
            except UnboundLocalError as e:
                print(e)
        return inner

    f = outer()
    try:
        f()     # exception raised
    except UnboundLocalError as e:
        print(e)

    print()

############################################################
# Part 2 - workaround for the above problem (mutable l-value)
def part2():
    def outer():
        x = [50]     # x is mutable and will be part of the closure
        def inner():
            displayClosures(inner)
            x[0] += 1  # x refers to outer 'x' because it's mutable => closure
            displayClosures(inner)
        return inner

    f = outer()
    f()         # NO exception raised
    print()

############################################################
# Part 3 - a better workaround for the above problem (nonlocal)
def part3():
    def outer():
        x = 50      # immutable local variable
        def inner():
            nonlocal x
            displayClosures(inner)
            x += 1  # x refers to outer.x
            displayClosures(inner)
        return inner

    f = outer()
    f()         # NO exception raised


part1()
part2()
part3()
