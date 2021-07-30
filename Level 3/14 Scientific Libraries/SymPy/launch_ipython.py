import os

ipython = "/Users/seddon/Anaconda3/anaconda/bin" + os.pathsep
os.environ["PATH"] = ipython + os.environ["PATH"]
os.system("ipython notebook")
