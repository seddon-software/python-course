import subprocess,os,sys
sys.path.append('../..')
import set_paths


os.chdir("../src")

# must run build first
os.system("python setup.py install")
