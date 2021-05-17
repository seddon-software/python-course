import subprocess,os,sys

def setPath():
    # Changing the PATH to locate C compiler
    mingwPath = "C:\mingw\bin;"
    os.environ["PATH"] = mingwPath + os.environ["PATH"]

setPath()
subprocess.call("gcc -g -Wall hello.c -o hello -IC:\Python26\include -LC:\Python26\libs -lpython26".split())
