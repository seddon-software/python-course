'''
Gotchas
========

When using a closure you capture to the Python reference and not its value.  When you come to use the reference
the value may have changed.  This can give rise to unexpected results.  

In part 1 of this example we build a list of function pointers in "funcs" in a loop where i is changing.  It looks
as though when we later call these functions they will all print out the different values of i that were in force
when the functions were added to the list, i.e. 1, 2, 3, 4.  This is not the case.  The 4 function pointers are
added to the list "funcs", but by the time they are called, i is now pointing to the immutable object 3.  Hence 
the print out: 3, 3, 3, 3.

In part 2, we make a small but subtle change.  Note the def
        def f(i=i):
This call uses named parameters.  The second pointer called i is a local variable pointing at the current value
of the outer i.  The assignment
        i=i
forces the interpreter to treat the first i as a local variable (its used as an l-value) and sets it to the
current value of i.  This local variable hides the global i and it dosen't change when the global i changes.  
Now the code behaves as expected and prints 0, 1, 2, 3.  Note that there "f" has no locals in part 1.
'''

############################################################
# Part 1 - closure gives 'unexpected' results
# Closures close over variables, not values
funcs = []
for i in range(4):
    def f():
        print(("locals for f(): ", locals()))
        print(i)    # this uses the global variable i
    funcs.append(f)

for f in funcs:
    f()             # i is now 3, so it prints 3 each time
print()

############################################################
# Part 2 - create extra instances of i for the closure
funcs = []
for i in range(4):
    def f(i=i):     # new i with local scope
        print(("locals for f(): ", locals()))
        print(i)    # each i takes on a different value
    funcs.append(f)
    
for f in funcs:
    f()             # prints 0, 1, 2, 3
print()

