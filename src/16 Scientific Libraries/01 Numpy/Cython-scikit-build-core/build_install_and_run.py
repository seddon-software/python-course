import os
os.system("export TERM=~/tmp")
os.system("python -m pipx run build")
os.system("python -m Spip install .")

import cythonRoots as roots
print(roots.sumOfRoots(10))

os.system("pip show cythonRoots")
print("spec of module")
print("==============")
print(roots.__spec__)


