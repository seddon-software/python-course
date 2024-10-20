import os

def execute(message, cmd):
    input(message)
    print("="*len(message))
    os.system(cmd)
    print()

execute(message="build extension module with pipx", cmd="pipx run build")
execute(message="install extension module with pip", cmd="pip install --force-reinstall .")
execute(message="test", cmd="")
import using_STL as s
s.hello("Chris")
s.goodbye("Chris")

import numpy as np
data1 = list(range(3, 15))
data2 = list(np.arange(3, 15.7, 0.1))
print(s.average(data1))
print(s.average2(data2))
print()

# clean up
execute(message="remove dist folder", cmd="rm -r dist")
