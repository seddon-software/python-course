'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, glob

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
call("python -m pip uninstall --yes cythonRoots")

call("python -m pip install .")

# test
printMessage("test Cython code")
import cythonRoots
print((cythonRoots.sumOfRoots(20)))

# clean up
printMessage("clean up")
call("rm -rf build")
call("rm -rf functions.egg-info")
call("tree .")
