import sys
import subprocess

# implement pip as a subprocess:
try:
    subprocess.run(f"{sys.executable} -m pip install --upgrade pip --user".split()) 
except CalledProcessError as e:
    print(e)
