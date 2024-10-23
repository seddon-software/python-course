import os

def execute(message, cmd):
    os.system("clear")
    input(message)
    print("="*len(message))
    print(f">>> {cmd}\n")
    os.system(cmd)
    print()
    input("continue?")

execute(message="clean", cmd="rm -r build")
execute(message="Build makefiles", cmd="cmake -S . -B build")
execute(message="Make shared library", cmd="cmake --build build")
execute(message="copy shared library", cmd="cp build/*.so .")

# clean up
execute(message="clean", cmd="rm -r build")
execute(message="files", cmd="tree .")
