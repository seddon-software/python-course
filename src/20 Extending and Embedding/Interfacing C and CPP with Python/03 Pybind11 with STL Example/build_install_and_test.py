'''
This script uses pip as a front end to build a C++ extension module as a whl file.
I've tried to use build because it uses a virtual environment, but this always fails to find header files
The script installs the wheel using pip as a back end.
'''

import os, subprocess, time, glob
N = 1

def printMessage(m):
    time.sleep(N)
#    subprocess.call(["clear"])
    print(m)
    print("-" *  len(m))
    print()
    input("?")

def call(cmd):
    print(cmd)
    time.sleep(N)
    subprocess.call(cmd.split())



'''
# Use CMake to build extension module
printMessage("Use CMake to build extension module")
call("cmake -S . -B build")
call("cmake --build build")
'''

# uninstall previous version
printMessage("uninstall previous version of extension module (if it exists)")
call("rm -rf build")
call("python -m pip uninstall --yes hello_goodbye_cpp")

# install new version
printMessage("install new version")
call("python -m pip install .")

# clean up
printMessage("clean up")
call("rm -rf build")
call("rm -rf hello_goodbye.egg-info")

# test in new folder
printMessage("test in new folder")
os.chdir("TestFolder")
call("python testit.py")
os.chdir("..")

# uninstall again
printMessage("uninstall again")
call("python -m pip uninstall --yes hello_goodbye_cpp")

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
call(f"rm -rf {eggFolder}")
call("python -m pip uninstall --yes hello_goodbye_cpp")

