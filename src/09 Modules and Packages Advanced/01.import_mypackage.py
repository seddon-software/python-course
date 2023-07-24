'''
A module is a single Python file, whereas a package is directory hierarchy holding several files.
Consult the accompanying Jupyter Notebook for full details on importing packages and modules.

Note that modules must be on the PYTHONPATH; the PYTHONPATH is an environment variable.  To temporarily add 
a folder to the PYTHONPATH write: 
            sys.path.append("mylib")
'''

import sys
sys.path.append("mylib")

for d in sys.path:
    print(d)

import mypackage


mypackage.f1()
mypackage.f2()
mypackage.f3()
mypackage.f4()



