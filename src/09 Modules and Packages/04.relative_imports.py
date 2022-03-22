'''
Relative Imports
================
In this example we have the following directory structure:

mylib2
└── app
    ├── __init__.py
    ├── sub1
    │   ├── __init__.py
    │   └── module1.py
    └── sub2
        ├── __init__.py
        └── module2.py

Note: Since Python 3.3, __init__.py is no longer required to define directories as importable Python packages.

Our package is "app" and this must be on the PYTHONPATH, so we need to:
            sys.path.append("mylib2")

Now we can import module1 in the normal way:
            import app.sub1.module1 as m1

Inside "module1" there is the following relative import:
            from ..sub2 import module2 as m2 # relative import
and call
            m2.f2()

and this loads module2 and allows us to call "m2.f2()".

With relative imports:
    . means that the module is in the current directory 
    .. means that it is in the directory above. 
    ... means that it is in the grandparent directory, and so on

This is similar to Unix relative paths:
    .       is like ./
    ..      is like ../
    ...     is like ../../
    ....    is like ../../../
'''

import sys
sys.path.append("mylib2")

print(f"This is module: {__name__}")
print(f"in package: {__package__}")
import app.sub1.module1 as m1


