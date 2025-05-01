import os, time

def execute(message, cmd):
    time.sleep(5)
    os.system("clear")
    input(message)
    print("="*len(message))
    os.system(cmd)
    print()

execute(message="build extension module with pipx", cmd="python -m pipx run build")
execute(message="install extension module with pip", cmd="python -m pip install --force-reinstall .")

execute(message="test", cmd="")
import roots as r
print(r.sumOfRoots(10))
print()

# clean up
execute(message="clean up", cmd="rm -r dist; tree .")
