import subprocess,os

os.chdir("../src/dist")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode().strip()
print(f"Installing {wheelFile}")
subprocess.call(f"python -m pip install --force-reinstall {wheelFile} --user".split())
