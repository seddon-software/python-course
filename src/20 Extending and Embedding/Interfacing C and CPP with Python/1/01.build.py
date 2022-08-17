import subprocess, os

cmd = "g++ -O3 -Wall -shared -std=c++20 -fPIC $(python3 -m pybind11 --includes) src/01.cpp -o Lib01.so"
os.system(cmd)
subprocess.run("ls -l *.so", shell=True)
