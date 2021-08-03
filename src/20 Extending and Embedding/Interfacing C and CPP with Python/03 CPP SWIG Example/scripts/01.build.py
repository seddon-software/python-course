import subprocess,os,sys
sys.path.append('../..')
import set_paths

os.system("swig -version")
os.chdir("../src")
os.system("python setup.py -v build_ext")
