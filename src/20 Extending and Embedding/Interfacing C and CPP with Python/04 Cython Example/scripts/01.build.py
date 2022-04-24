import subprocess,os

os.chdir("../scripts")
subprocess.call("python -m build -n ../src".split())
subprocess.call("tree ..".split())


