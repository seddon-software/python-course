import mylib as m
print(f"lib: {__name__}")


def f1():
    print("local f1")

from mylib import (f1, f2, f3, f4)

f1()
f2()
f3()
f4()

m.f1()
m.f2()
m.f3()
m.f4()
