print(f"This is module: {__name__}")
print(f"in package: {__package__}")

print("Now peforming a relative import of module2 ...")
print("\twith the line: from ..sub2 import module2 as m2")
from ..sub2 import module2 as m2 # relative import

m2.f2()


