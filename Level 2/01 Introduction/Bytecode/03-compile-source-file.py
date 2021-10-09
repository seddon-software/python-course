import py_compile, os

# compile only: creates .pyc
py_compile.compile("myfile.py")
os.system("ls -lR myfile.* __pycache__")

