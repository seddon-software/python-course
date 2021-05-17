import subprocess,os,sys
sys.path.append('../..')
import set_paths

os.environ["ARCHFLAGS"] = "-arch x86_64"

os.system("swig -version")
os.chdir("../src")
subprocess.call('python setup.py -v build_ext'.split())
