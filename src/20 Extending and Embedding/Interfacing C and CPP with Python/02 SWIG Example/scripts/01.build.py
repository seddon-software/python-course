import subprocess,os


os.chdir("../src")
subprocess.call("swig -python hello.i".split())
os.chdir("../scripts")
subprocess.call("python -m build -n ../src".split())
subprocess.call("tree ..".split())


