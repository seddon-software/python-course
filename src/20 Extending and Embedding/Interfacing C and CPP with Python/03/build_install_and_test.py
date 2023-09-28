import os, subprocess, time, glob

def printMessage(m):
    time.sleep(5)
    subprocess.call(["clear"])
    print(m)
    print("-" *  len(m))
    print()
    input("?")

def call(cmd):
    print(cmd)
    time.sleep(5)
    subprocess.call(cmd.split())


# Use CMake to build extension module
printMessage("Use CMake to build extension module")
call("rm -rf build")
call("cmake -S . -B build")
call("cmake --build build")

# uninstall previous version
printMessage("uninstall previous version of extension module (if it exists)")
call("python -m pip uninstall --yes hello_goodbye_cpp")

# install new version
printMessage("install new version")
call("python -m pip install -e .")

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
#call("python setup.py bdist_wheel --universal")
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
call(f"rm {glob.glob('*.so')[0]}")

