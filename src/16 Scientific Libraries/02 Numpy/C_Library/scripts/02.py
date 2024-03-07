import subprocess,os,sys

print("Installing fibonacci module")
os.chdir("../src/dist")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode().strip()
subprocess.call(f"python -m pip install --force-reinstall {wheelFile}".split())
