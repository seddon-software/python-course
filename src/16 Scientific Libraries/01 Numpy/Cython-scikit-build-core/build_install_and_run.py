import os
os.system("pipx run build")
os.system("pip install .")

import cythonRoots as roots
print(roots.sumOfRoots(10))

os.system("pip show cythonRoots")
print("spec of module")
print("==============")
print(roots.__spec__)


