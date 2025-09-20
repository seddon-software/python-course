'''
Gotchas
========

Closures are over variable names, not values.  What this means in this example is that for the four functions
f() there is a closure over the name "f".  In other words a single closure is associated with the symbol "f"
and this is shared by all four functions f().

As you step through this code you will see that the name "f" has a single closure cell with a reference to i.
Inside the for loop this cell changes each time f() is redefined.  At the end of the loop the closure 
contains a reference to the last integer i defined by the for loop.

In this example we build a list of function pointers in "funcs" in a loop where i is changing.  It looks
as though when we later call these functions they will all print out the different values of i that were in 
force when the functions were added to the list, i.e. 1, 2, 3, 4.  This is not the case.  The 4 function 
pointers are added to the list "funcs" all have the same name and hence share the closure and by the time 
they are called, the closure refers to the immutable object 3.  Hence the print out: 
            3, 3, 3, 3,
'''


from utils import *     # for displayClosures

############################################################
# Closures are over variable names, not values
def main():
    funcs = []
    # note that because i is immutable as we go round the loop, i points to different int objects
    # this in turn means that the closure for the name(symbol) "f" will change
    for i in range(4):
        def f():
            print(i, end=',')
        funcs.append(f)
        print("closures in funcs:")
        [displayClosures(f) for f in funcs]
        print()
        # notice how the closure cells in funcs build up as we step through the loop
        # each of the 4 function "f"s close on the symbol "i" not on its value
        # at the end of the loop the value of "i" is 3, so all 4 function "f"s see this value

    for f in funcs:
        # the closure on "f" is now on the fourth integer object (i = 3)
        f()             # i is now 3, so it prints 3 each time
    print()

main()
