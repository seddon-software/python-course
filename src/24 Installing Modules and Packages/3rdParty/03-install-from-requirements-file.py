import sys
import subprocess
try:
    subprocess.run(f"{sys.executable} -m pip install -r requirements.txt --user".split()) 
except CalledProcessError as e:
    print(e)


