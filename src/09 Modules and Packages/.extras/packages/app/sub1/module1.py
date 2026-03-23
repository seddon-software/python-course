print(f"This is module: {__name__} in package: {__package__}")

print("Now performing a relative import of module2")
from ..sub2 import module2 as m2 # relative import


def f1():
    m2.f2()

