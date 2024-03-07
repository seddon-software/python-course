import os, subprocess
os.chdir("../src")
subprocess.call("python -m build --no-isolation .".split())
