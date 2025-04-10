'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, time, glob

if_build_failed = """if the build fails because of 'failed to map segment from shared object'
you need to run: 
\texport TERM=~/tmp"""
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
    result = subprocess.run(cmd.split())
    try:
        result.check_returncode()
    except Exception as e:
        print(e)
        print(if_build_failed)
        sys.exit(1)

call ("clear")    

printMessage("build with pipx")
call("python -m pipx run build")

printMessage("install with pip")
os.system("python -m pip install .")

printMessage(f"test module: {MODULE}")

import cythonRoots as roots
print(f"result = {roots.sumOfRoots(10)}")

printMessage("pip show")
call("python -m pip show cythonRoots")
printMessage("spec of module")
print(roots.__spec__)

printMessage("clean up")
call("rm -rf dist")
call("tree .")
