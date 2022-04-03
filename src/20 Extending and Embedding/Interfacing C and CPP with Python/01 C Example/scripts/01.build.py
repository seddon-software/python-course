import subprocess,os,sys
sys.path.append('../..')
import set_paths


#os.chdir("..")
#subprocess.call("python -m build -h".split())
subprocess.call("python -m build --outdir=build ../src".split())
subprocess.call("tree ..".split())
