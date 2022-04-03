import os, subprocess, shutil

subprocess.call("tree ..".split())
try:
    shutil.rmtree("build")
    print("build directory removed")
except:
    print("build directory already removed")
os.chdir("../src")
response = subprocess.run("ls -d *.egg-info", shell=True, capture_output=True)
eggDir = response.stdout.decode().strip()
try:
    shutil.rmtree(eggDir)
    print("Egg File directory removed")
except:
    print("Egg File directory already removed")
subprocess.call("tree ..".split())

