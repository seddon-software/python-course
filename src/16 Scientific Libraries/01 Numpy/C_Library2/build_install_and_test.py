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
call("python -m pip uninstall --yes roots")

# create shared object using cmake
printMessage("build shared object with cmake")
call("cmake -S . -B build")
call("cmake --build build")


# build wheel
printMessage("build wheel")
call("python -m pip wheel -e .")

# install wheel
printMessage("install wheel")
wheelFile = glob.glob("*.whl")[0]
call(f"python -m pip install --force-reinstall {wheelFile}")
call(f"python --version")

import site
sitePackages = site.getsitepackages()[0]
sitePackages = site.USER_SITE
printMessage(f"copy shared object to site packages: {sitePackages}")
sharedObject = glob.glob("build/*.so")[0]
call(f"cp {sharedObject} {sitePackages}")

# test
printMessage("test roots")
import roots
print(f"result: {roots.sumOfRoots(10)}")

# clean up
printMessage("clean up")
# call("rm -rf dist")
call("rm -rf build")
call("rm -rf CMakeFiles")
call(f"rm {wheelFile}")
# eggFolder = glob.glob("*.egg-info")[0]
call("rm -rf roots.egg-info")
call("tree .")

