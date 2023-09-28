from invoke import task, Context

source = "hello_goodbye"
python_version = "python3.9"

@task
def build(c):
    c.run(
       f"g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC {source}.cpp "
       f"-o libhello_goodbye.so ", echo=True)

@task
def run(c):
    c.run( f"g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC " 
    "-I /usr/include/python3.9 -I .  " 
    "$(python3 -m pybind11 --includes) "
    f"hello_goodbye_wrapper.cpp " 
    f"-o {source}$({python_version}-config --extension-suffix) "
    "-L. -lhello_goodbye -Wl,-rpath,.", echo=True)

@task
def go(c):
    c.run("python testit.py", echo=True)

c = Context()
build(c)
run(c)
go(c)
