import subprocess,os

os.chdir("../src/dist")
subprocess.call("tree".split())
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode().strip()
print(f"Uninstalling {wheelFile}")
subprocess.call(f"python -m pip uninstall -y {wheelFile}".split())





