import subprocess,os,sys

print("Uninstalling fibonacci module")
os.chdir("../src/dist")
subprocess.call("tree".split())
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode()
subprocess.call(f"python -m pip uninstall -y {wheelFile}".split())
