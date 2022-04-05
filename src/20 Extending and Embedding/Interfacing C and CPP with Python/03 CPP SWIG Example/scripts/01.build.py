import subprocess,os

os.chdir("../src")
subprocess.call("swig -c++ -python -cppext cpp myexample.i".split())
os.chdir("../scripts")
subprocess.call("python -m build -n ../src".split())
subprocess.call("tree ..".split())


