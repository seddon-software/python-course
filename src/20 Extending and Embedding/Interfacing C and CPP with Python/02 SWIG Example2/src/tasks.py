from invoke import task

@task
def build(c, docs=False):
    c.run(
       "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC hello.c "
    "-o libcppmult.so ")

@task
def run(c, docs=False):
    c.run( f"g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC " 
    "-I/opt/anaconda3/include/python3.9 -I/opt/anaconda3/lib/python3.9/site-packages/pybind11/include "
    "-I /usr/include/python3.9 -I .  " 
    f"pybind11_wrapper.cpp " 
    f"-o pybind11_example.cpython-39-x86_64-linux-gnu.so "
    "-L. -lcppmult -Wl,-rpath,.")
