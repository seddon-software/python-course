import os

def remove(target, options=""):
    print(f"removing {target}")
    os.system(f"rm {options} {target}")

os.chdir("../src")
remove("dist", "-r")
remove("hello_wrap.c")
remove("myhello.py")
remove("SWIGexample.egg-info", "-r")
print("staging area cleaned")


