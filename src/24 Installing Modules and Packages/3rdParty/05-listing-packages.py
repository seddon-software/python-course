import sys
import subprocess

try:
    subprocess.run(f"{sys.executable} -m pip list".split()) 
    subprocess.run(f"{sys.executable} -m pip list --outdated".split()) 
    subprocess.run(f"{sys.executable} -m pip show beautifulsoup4".split()) 
except CalledProcessError as e:
    print(e)
