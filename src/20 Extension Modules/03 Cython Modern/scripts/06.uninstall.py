import subprocess, os

os.chdir("..")
subprocess.run("pip uninstall -y cython_functions".split())
