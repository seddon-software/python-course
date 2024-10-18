import os, subprocess

def remove(target, options=""):
    print(f"removing {target}")
    subprocess.run(f"rm {options} {target}", shell=True)

os.chdir("../src")
remove("dist", "-r")
remove("build", "-r")
remove("functions.c")
remove("*.egg-info", "-r")
print("staging area cleaned")



