import subprocess, os

# build shared library
cmd = "g++ -O3 -Wall -shared -std=c++20 -fPIC $(python3 -m pybind11 --includes) src/02.cpp -o Lib02.so"
os.system(cmd)

# look at C++ demangled names
subprocess.run("nm Lib02.so | egrep '(add|display)' | c++filt", shell=True)

# display shared libraries
subprocess.run("ls -l *.so", shell=True)
