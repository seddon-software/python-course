import os, subprocess

def remove(target, options=""):
    print(f"removing {target}")
    subprocess.run(f"rm {options} {target}", shell=True)

os.chdir("../src")
remove("dist", "-r")
remove("*.egg-info", "-r")
print("staging area cleaned")

print("see what files are present after uninstalling and cleaning")
subprocess.call("tree ..".split())

