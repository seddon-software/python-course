'''
This test program accesses the library using both 'import' and 'from'.  In practice you would only use one of 
these methods.

Note the use of the alias ff1 to avoid name clashes.
'''

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
