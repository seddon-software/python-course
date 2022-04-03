import subprocess,os,sys
sys.path.append('../..')
import set_paths

subprocess.call("tree".split())
os.chdir("build")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode()
subprocess.call(f"python -m pip uninstall -y {wheelFile}".split())
