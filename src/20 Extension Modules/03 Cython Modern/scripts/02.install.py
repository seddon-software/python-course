import subprocess, os

os.chdir("..")
subprocess.run("pip install .".split())
