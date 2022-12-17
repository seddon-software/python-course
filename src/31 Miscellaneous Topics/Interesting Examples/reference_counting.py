############################################################
#
#    Reference counting
#
############################################################

import sys

class MyClass:
    def __del__(self):
        print("DTOR")

p1 = MyClass()  # ref count: 1
p2 = p1         # ref count: 2
p3 = p1         # ref count: 3

print(sys.getrefcount(p1)) # typically one higher than expected
 
p1 = None       # ref count: 2
p2 = None       # ref count: 1
p3 = None       # ref count: 0 => DTOR called


