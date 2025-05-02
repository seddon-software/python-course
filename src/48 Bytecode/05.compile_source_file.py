'''
The Bytecode Cache
==================

The py-compile module allows us to compile source code and produce a bytecode file.  The resulting file will have
a .pyc extension.  This is the file you will sometimes find in the __pycache__ folder.  It is never necessary to
compile source code ourselves; CPython will compile code automatically to refresh the cache.  Indeed, we are only
compiling this code to show what gets put in the cache.
'''

import os, py_compile
py_compile.compile("myfile.py")

# compiled files are placed in the cache
os.system("hexdump __pycache__/*.pyc")
os.system("file __pycache__/*.pyc")
os.system("ls -l __pycache__")
