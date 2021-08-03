import os, shutil, sys

def s(*cmds):
    cmd = " ".join(cmds)
    print(">>> {}".format(cmd), end="")
    input()
    if cmd[0:2] == "cd":
        os.chdir(cmd[3:])
    else:
        os.system(cmd)

djangoAdmin = "/Users/seddon/Anaconda3/anaconda/bin" + os.pathsep
python = os.path.dirname(sys.executable) + os.pathsep
os.environ["PATH"] = djangoAdmin + os.environ["PATH"]
os.environ["PATH"] = python + os.environ["PATH"]

