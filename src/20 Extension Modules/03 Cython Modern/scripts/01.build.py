import subprocess, os

os.chdir("..")
subprocess.call("pipx run build".split())


