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
call("python -m pip uninstall --yes hello_goodbye")

# install new version
printMessage("install new version")
call("python setup.py install")

# clean up
printMessage("clean up")
call("rm -rf build")
#rm -rf dist
call("rm -rf hello_goodbye.egg-info")

# test in new folder
printMessage("test in new folder")
os.system("pwd")
os.chdir("TT")
call("python testit.py")
os.chdir("..")

# uninstall again
printMessage("uninstall again")
call("python -m pip uninstall --yes hello_goodbye")

# build wheel
printMessage("build wheel")
call("python setup.py bdist_wheel --universal")

# install wheel
printMessage("install wheel")
wheelFile = glob.glob("dist/*.whl")[0]
call(f"python -m pip install {wheelFile}")


# test again
printMessage("test again")
os.chdir("TT")
call("python testit.py")
os.chdir("..")

# clean up
printMessage("clean up")
call("rm -rf dist")
