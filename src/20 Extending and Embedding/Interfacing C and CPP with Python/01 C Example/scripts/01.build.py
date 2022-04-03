import subprocess,os,sys

subprocess.call("python -m build --outdir=build ../src".split())
subprocess.call("tree ..".split())
