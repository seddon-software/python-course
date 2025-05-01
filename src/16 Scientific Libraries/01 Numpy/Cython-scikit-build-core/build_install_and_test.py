'''
Run this script from the command line (difficult to read output in VSCode)
'''

import os, sys, subprocess, time, glob

if_build_failed = """if the build fails because of 'failed to map segment from shared object'
you need to run: 
\texport TEMP=~/tmp"""
N = 0
MODULE = "cythonRoots"

def printMessage(m):
    print()
    print(m)
    print("-" *  len(m))
    print()
    input("?")

# def call(cmd):
#     print(cmd)
#     time.sleep(N)
#     result = subprocess.run(cmd.split())
#     try:
#         result.check_returncode()
#     except Exception as e:
#         print(e)
#         print(if_build_failed)
#         sys.exit(1)

def execute(message, cmd):
    time.sleep(1)
    os.system("clear")
    input(message)
    print("="*len(message))
    result = subprocess.run(cmd.split())
    try:
        result.check_returncode()
    except Exception as e:
        print(e)
        print(if_build_failed)
        sys.exit(1)
#    os.system(cmd)
    print()

execute(message="build with pipx", cmd="python -m pipx run build")
execute(message="install with pip", cmd="python -m pip install .")

printMessage(f"test module: {MODULE}")
import cythonRoots as roots
print(f"result = {roots.sumOfRoots(10)}")

execute(message="pip show", cmd="python -m pip show cythonRoots")
printMessage("spec of module")
print(roots.__spec__)

# clean up
execute(message="clean up", cmd="rm -r dist")
execute(message="tree", cmd="tree .")

