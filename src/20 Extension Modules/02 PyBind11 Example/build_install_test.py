import os
os.system("pipx run build")
os.system("pip install .")
os.system("rm -r dist")
import sumOfRoots as roots
print(roots.sumOfRoots(10))

