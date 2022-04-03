import subprocess,os,sys

print("Installing fibonacci module")
os.chdir("build")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode()
subprocess.call(f"python -m pip install {wheelFile}".split())
