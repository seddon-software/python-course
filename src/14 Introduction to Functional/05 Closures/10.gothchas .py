'''
Gotchas
========

The problems with the closure in the previous example can be overcome by making the "i" parameter a local 
variable.  All you need to do is to pass "i" as a parameter to the function "f":
        def f(i=i):

This assignment forces the interpreter to treat the first i as a local variable (its used as an l-value) and 
sets it to the current value of i.  This local variable hides the loop count "i" and Python remembers its
initial value even when the loop count changes.

Now the code behaves as expected and prints 0, 1, 2, 3.
'''

import os
os.system("clear")

def displayClosures(fn):
    try:
        for cell in fn.__closure__:
            print(f"{fn.__name__}:{cell}")
    except:
        print(f"{fn.__name__}:closure is empty")

############################################################
# 
def main():
    funcs = []
    for i in range(4):
        def f(i=i):             # this creates a local variable i (initialised with the current loop count)
            print(locals())
            print(i)    # this i refers to a local and not to a closure
        displayClosures(f)
        funcs.append(f)

    for f in funcs:
        f()

main()
