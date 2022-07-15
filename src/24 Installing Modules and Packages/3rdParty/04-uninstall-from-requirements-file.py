import sys, os
import subprocess

try:
    subprocess.run(f"{sys.executable} -m pip uninstall -r requirements.txt -y".split()) 
except CalledProcessError as e:
    print(e)

