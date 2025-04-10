'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, time, glob

N = 0
MODULE = "cythonRoots"

def printMessage(m):
    time.sleep(N)
    print()
    print(m)
    print("-" *  len(m))
    print()
    input("?")

def call(cmd):
    print(cmd)
    time.sleep(N)
    subprocess.call(cmd.split())


call ("clear")    
# remove old build folders
printMessage("remove old build folders")
call("rm -rf build")

# uninstall previous version
printMessage("uninstall previous version of extension module (if it exists)")
call(f"python -m pip uninstall --yes {MODULE}")

# install cython extension module
printMessage("install cython extension module")
call("python setup.py build_ext --inplace")

# test
printMessage("test cythonRoots")
import cythonRoots
print(f"compute: {f'{MODULE}.sumOfRoots(50)'}")
print(f"result: {cythonRoots.sumOfRoots(50)}")

# clean up
printMessage("clean up")
call(f"rm {MODULE}.c")
call("tree .")

print("spec of module")
print("==============")
print(cythonRoots.__spec__)




