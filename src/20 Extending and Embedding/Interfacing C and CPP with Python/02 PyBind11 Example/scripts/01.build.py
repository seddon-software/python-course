import subprocess,os


os.chdir("../src")
subprocess.call("invoke -e build".split())
subprocess.call("invoke -e run".split())
# os.chdir("../scripts")
# subprocess.call("python -m build -n ../src".split())
subprocess.call("tree ..".split())


