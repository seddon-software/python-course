import subprocess,os,sys

print("Egg info")
print("========")
os.chdir("../src")
response = subprocess.run("ls *.egg-info/PKG-INFO", shell=True, capture_output=True)
eggFile = response.stdout.decode()
subprocess.call(f"cat {eggFile}".split())

