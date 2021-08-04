############################################################
#
#    main.py
#
############################################################

import sys
sys.path.append("mylib")
print(sys.path)

import package1.package2.ModuleA as A
import package1.package2.ModuleB as B
import package1.package2.ModuleC as C

a = A.A()
b = B.B()
c = C.C()

a.f()
a.g()
a.h()

b.f()
b.g()
b.h()

c.f()
c.g()
c.h()
