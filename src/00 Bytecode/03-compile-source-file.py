import py_compile, os

# it is never necessary to compile source code - we are only doing it to show what gets put in the cache
py_compile.compile("myfile.py")

# compiled files are placed in the cache
os.chdir("__pycache__")
os.system("ls -l .")
os.system("hexdump *.pyc")

