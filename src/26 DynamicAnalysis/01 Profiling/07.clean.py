import os, shutil

try:
    shutil.rmtree("html")
except:
    pass

try:
    shutil.rmtree("stats")
except:
    pass

try:
    shutil.rmtree("__pycache__")
except:
    pass