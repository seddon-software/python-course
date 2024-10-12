'''
This script uses pip as a front end to build a C++ extension module as a whl file.
I've tried to use build because it uses a virtual environment, but this always fails to find header files
The script installs the wheel using pip as a back end.
'''

'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, time, glob

N = 1

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

name = "hello_goodbye_cpp"
os.chdir("src")

# remove old build folders
printMessage("remove old build folders")
call("tree .")
call("rm -rf build")

# uninstall previous version
printMessage("uninstall previous version of extension module (if it exists)")
call(f"python -m pip uninstall --yes {name}")

# install new version
printMessage("install new version")
call("python -m pip install -e .")

# test in new folder
printMessage("test in new folder")
os.chdir("TestFolder")
call("python testit.py")
os.chdir("..")

# clean up
printMessage("clean up before building wheel")
call("rm -rf build")
call(f"rm -rf {name}.egg-info")
soFile = glob.glob('*.so')[0]
call(f"rm -rf {soFile}")
call("tree .")

# build wheel
printMessage("build wheel")
call("python -m pip wheel -e .")

# install wheel
printMessage("install wheel")
wheelFile = glob.glob("*.whl")[0]
call(f"python -m pip install {wheelFile}")

# test again
printMessage("test again")
os.chdir("TestFolder")
call("python testit.py")
os.chdir("..")

# clean up
printMessage("clean up")
call("rm -rf dist")
call("rm -rf build")
call(f"rm {wheelFile}")
eggFolder = glob.glob("*.egg-info")[0]
call(f"rm -rf {name}.egg-info")
call("tree .")

