import subprocess,os,sys
import set_paths

# Note that you need to install Swig to get these examples to work:
#   https://www.dev2qa.com/how-to-install-swig-on-macos-linux-and-windows/

os.chdir("../src")
os.system("python setup.py -v build_ext")



