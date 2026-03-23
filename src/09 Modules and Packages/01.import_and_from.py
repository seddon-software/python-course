'''
A module is a single Python file that contains a library of functions an/or classes.  
A package is a set of Python files that contains a library.

Each Python file contains a symbol table that contains all the names used in the library.  When you want to use 
a module you need to access or import its contents via its symbol table.

There are two different ways of accessing this symbol table:
    import
    from

With 'import' as in:
    import mylib as m

you have to qualify all symbols with the library name (mylib) or its alias (m).  Note the library name is always 
the file name with the .py extension removed.  For example:
    m.f1()

calls the function f1 in the mylib (alias m) module.

Alternatively, you can use 'from'.  In this case the library's symbol table is imported into the local symbol 
table, possibly overriding other symbol definitions.  Using 'from' is popular because you can then use 
unqualified names, but 'import' is clearer and doesn't pollute the local namespace. 

=============================================================================================

This test program accesses the library using both 'import' and 'from'.  In practice you would only use one of 
these methods.

Note the use of the alias ff1 to avoid name clashes.

Note that modules must be on the PYTHONPATH; the PYTHONPATH is an environment variable.  To temporarily add 
a folder to the PYTHONPATH write: 
            sys.path.append("mylib")
'''

import sys
sys.path.append("modules")

import mylib as m
from mylib import f1 as ff1, f2, f3, f4

def f1():
    print("local f1()")

ff1()
f1()
f2()
f3()
f4()
m.f1()
m.f2()
m.f3()
m.f4()


