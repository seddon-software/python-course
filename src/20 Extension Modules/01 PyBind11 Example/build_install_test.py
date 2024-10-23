import os

def execute(message, cmd):
    os.system("clear")
    input(message)
    print("="*len(message))
    print(f">>> {cmd}\n")
    os.system(cmd)
    print()
    input("continue?")

execute(message="build extension module with pipx", cmd="pipx run build")
execute(message="install extension module with pip", cmd="pip install --force-reinstall .")

print("test")
print("====")
import using_STL as s
s.hello("Chris")
s.goodbye("Chris")

import numpy as np
data1 = list(range(3, 15))
data2 = list(np.arange(3, 15.7, 0.1))
print(s.average(data1))
print(s.average2(data2))
print()
input("continue?")

# clean up
execute(message="clean up", cmd="rm -r dist")
