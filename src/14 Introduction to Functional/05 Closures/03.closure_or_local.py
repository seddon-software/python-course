import os; os.system("clear")
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

from utils import *     # for displayClosures


def main():
    x1 = ["mx1"]               # mutable
    x2 = ["mx2"]               # mutable
    y1 = "my1"                 # immutable
    y2 = "my2"                 # immutable
    y3 = "my3"                 # immutable
    print(f"main symbol table: {list(locals().keys())}")

    def f():
        # note y1 and y2 are locals, not closures
        # y3 is used as an r-value and is part of the closure
        print(f"f symbol table: {list(locals().keys())}")
        displayClosures(f)
        x1[0] = "fx1"
        x2[0] = "fx2"
        y1 = "fy1"
        y2 = y3
        displayClosures(f)
    f()

main()
