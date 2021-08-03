import py_compile, os

py_compile.compile("myfile.py")
os.system("ls -lR --full-time myfile.* __pycache__")

