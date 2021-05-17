import subprocess,os,sys

sys.path.append('../..')
import set_paths
os.chdir("../src")

installedFiles = open("files.txt", "r")
for file in installedFiles:
    subprocess.call(f"rm {file}".split())

subprocess.call("rm files.txt".split())
print()
print("Example uninstalled")




