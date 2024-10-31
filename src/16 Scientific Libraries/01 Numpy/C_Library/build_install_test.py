import os, time

def execute(message, cmd):
    time.sleep(5)
    os.system("clear")
    input(message)
    print("="*len(message))
    os.system(cmd)
    print()

execute(message="build extension module with pipx", cmd="pipx run build")
execute(message="install extension module with pip", cmd="pip install --force-reinstall .")

execute(message="test", cmd="")
import roots as r
print(r.sumOfRoots(10))
print()

# clean up
execute(message="remove dist folder", cmd="rm -r dist;tree .")
