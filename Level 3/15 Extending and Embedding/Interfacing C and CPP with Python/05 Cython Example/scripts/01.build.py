import os, sys
sys.path.append('../..')
import set_paths

os.system("swig -version")
os.system("python --version")
os.chdir("../src")
#os.system("python setup.py build_ext --inplace")
os.system("python setup.py build_ext")
