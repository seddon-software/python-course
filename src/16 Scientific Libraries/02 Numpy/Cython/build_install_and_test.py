'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, time, glob

N = 0

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
call("python -m pip uninstall --yes functions")

# build wheel
printMessage("build wheel")
call("python -m pip wheel -e .")

# install wheel
printMessage("install wheel")
wheelFile = glob.glob("*.whl")[0]
call(f"python -m pip install --force-reinstall {wheelFile}")
call(f"python --version")

# test
printMessage("test Cython code")
import functions
functions.say_hello()
functions.say_goodbye()
print((functions.fibonacci(100000)))
print((functions.sumOfSquares(2, 4)))

# clean up
printMessage("clean up")
# call("rm -rf dist")
call("rm -rf build")
call(f"rm {wheelFile}")
eggFolder = glob.glob("*.egg-info")[0]
call(f"rm -rf {eggFolder}")
call("tree .")

