'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, glob

file = "cythonRoots"

def printMessage(m):
    print()
    print(m)
    print("-" *  len(m))
    print()
    input("?")

def call(cmd):
    print(cmd)
    subprocess.call(cmd, shell=True)


call ("clear")    

# uninstall previous version
printMessage("uninstall previous version of extension module (if it exists)")
call(f"python -m pip uninstall --yes {file}")

call("python -m pip install .")

# clean up
printMessage("clean up")
call("rm -rf build")
call(f"rm -rf {file}.egg-info")
call("rm -rf dist")
call(f"rm {file}.c")
call("tree .")

# test
printMessage("test Cython code")
import cythonRoots
print(f"{cythonRoots.sumOfRoots(20):.4f}")
