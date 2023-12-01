'''
Closure or Local
================

Nested functions have access to their environment using closures.  However, this only applies to mutable items
or immutable items that are used as r-values (appear on the right hand sign of = or passed to other functions, 
such as print()).

In the example below, the nested function uses variables y1 and y2.  Since these are defined in the parent 
function its tempting to think they are part of the closure.  However, since we are assigning values to 
y1 and y2, we can't be referring to the parent's y1 and y2 as they are immutable.  In fact y1 and y2 are 
local variables.

Note that y3 is also immutable, but is used as an r-value (i.e. just read) and is therefore part of the 
closure and not a local variable.  Note that y3 is referenced in f() and therefore is listed as part of the
local symbol table of f() by the locals() built in.
'''

import os
os.system("clear")

def closures(fn):
    for c in fn.__closure__:
        print(f"closure for {fn.__name__}: {c} {c.cell_contents}")

def main():
    x1 = [1, 1, 1, 1]         # mutable
    x2 = [2, 2, 2, 2]         # mutable
    y1 = "y1"                 # immutable
    y2 = "y2"                 # immutable
    y3 = "y3"                 # immutable
    print(f"main symbols: {list(locals().keys())}")

    def f():
        # note y1 and y2 are locals, not closures
        # y3 is used as an r-value and is part of the closure
        x1[0] = 1
        x2[1] = 2
        y1 = "y1"
        print(f"f symbols: {list(locals().keys())}")
        y2 = y3
        closures(f)
        pass
    f()

main()
