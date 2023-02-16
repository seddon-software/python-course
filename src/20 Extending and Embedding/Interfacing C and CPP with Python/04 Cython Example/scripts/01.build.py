import subprocess,os

os.chdir("../scripts")
subprocess.call("python -m build --wheel -n ../src".split())
subprocess.call("tree ..".split())


