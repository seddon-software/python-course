import subprocess, os

def execute(message, cmd):
    os.system("clear")
    input(message)
    print("="*len(message))
    os.system(cmd)
    print()
    input("continue?")

execute(message="build extension module", cmd="pipx run build")
execute(message="install extension module", cmd="pip install .")

os.system("clear")
print("test")
print("====")
import cython_functions as cf
cf.say_hello()
cf.say_goodbye()
print((cf.fibonacci(100000)))
print((cf.sumOfSquares(2, 4)))
print()
input("continue?")

execute(message="", cmd="python timings.py")
execute(message="uninstall", cmd="pip uninstall -y cython_functions")
execute(message="clean", cmd="rm -r dist; rm -r __pycache__; tree .")


