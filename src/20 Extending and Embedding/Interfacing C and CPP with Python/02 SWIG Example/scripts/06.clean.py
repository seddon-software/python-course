import os, subprocess

def remove(target, options=""):
    print(f"removing {target}")
    subprocess.run(f"rm {options} {target}", shell=True)

os.chdir("../src")
remove("dist", "-r")
remove("hello_wrap.c")
remove("myhello.py")
remove("*.egg-info", "-r")
print("staging area cleaned")


