'''
A More Complex Example
======================
In this example we have the following directory structure:

MoreComplexExample
└── mylib
    └── package1
        ├── __init__.py
        ├── package2
        │   ├── __init__.py
        │   ├── ModuleA.py
        │   ├── ModuleB.py
        │   └── ModuleC.py
        └── package3
            ├── __init__.py
            └── ModuleD.py

Note the packages all reside in MoreComplexExample/mylib.  For Python to locate the packages you must add this 
folder to the PYTHONPATH.  This can be achieved with:

            sys.path.append("MoreComplexExample/mylib")
'''

import sys
sys.path.append("MoreComplexExample/mylib")
print(sys.path)

import os
os.system("tree MoreComplexExample -I __pycache__")
import package1.package2.ModuleA as A
import package1.package2.ModuleB as B
import package1.package2.ModuleC as C

# create objects
a = A.A()
b = B.B()
c = C.C()

# call methods
a.f()
a.g()
a.h()

b.f()
b.g()
b.h()

c.f()
c.g()
c.h()
