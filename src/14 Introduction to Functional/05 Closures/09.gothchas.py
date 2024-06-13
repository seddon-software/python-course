'''
Gotchas
========

Closures are over variable names, not values.  What this means in this example is that for the four functions
f() there is a closure over the name "f".  In other words a single closure is associated with the symbol "f"
and this is shared by all four functions f().

As you step through this code you will see that the name "f" has a single colusre cell with a reference to i.
Inside the for loop this cell changes each time f() is redefined.  At the end of the loop the closure 
contains a reference to the last integer i defined by the for loop.

In this example we build a list of function pointers in "funcs" in a loop where i is changing.  It looks
as though when we later call these functions they will all print out the different values of i that were in 
force when the functions were added to the list, i.e. 1, 2, 3, 4.  This is not the case.  The 4 function 
pointers are added to the list "funcs" all have the same name and hence share the closure and by the time 
they are called, the closure refers to the immutable object 3.  Hence the print out: 
            3, 3, 3, 3,
'''

import os
os.system("clear")

from utils import *

############################################################
# Closures are over variable names, not values
def main():
    funcs = []
    # note that because i is immutable as we go round the loop, i points to different int objects
    # this in turn means that the closure for the name(symbol) "f" will change
    for i in range(4):
        # notice how the closure cell on the name "f" changes as we step through the loop
        # although we create 4 function objects in the loop, we only have one name "f" and hence
        # a single closure cell.  Note the address of the closure cell doesn't change.
        print(f"int object i is at {id(i):X}")
        def f():
            print(i, end=", ")
        displayClosures(f)
        funcs.append(f)
    # at the end of the loop the closure on "f" is set to latest function object and the closure
    # on "i" is set to the latest int object (i=3)

    # funcs now contains 4 function pointers, but there is only one closure for "f"

    for f in funcs:
        # the closure on "f" is now on the fourth integer object (i = 3)
        f()             # i is now 3, so it prints 3 each time
    print()

main()
