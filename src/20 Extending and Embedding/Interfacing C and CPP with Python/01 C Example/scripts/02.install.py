import subprocess,os,sys
sys.path.append('../..')
import set_paths

os.chdir("build")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode()
print(wheelFile)
subprocess.call(f"python -m pip install {wheelFile}".split())
