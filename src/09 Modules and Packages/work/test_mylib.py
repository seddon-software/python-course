print(__name__)
import mylib as m


def f1():
    print("local")
from mylib import (f1, f2)

f1()
f2()
m.f3()
m.f4()
