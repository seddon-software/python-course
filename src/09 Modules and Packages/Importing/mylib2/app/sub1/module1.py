print("I am module 1")

print(__name__)
print(__package__)
from ..sub2 import module2 as m2 # relative import

m2.f2()


