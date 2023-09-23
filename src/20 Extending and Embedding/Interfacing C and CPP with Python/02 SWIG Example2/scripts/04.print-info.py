import subprocess,os

os.chdir("../src")
response = subprocess.run("cat *.egg-info/PKG-INFO", shell=True)
