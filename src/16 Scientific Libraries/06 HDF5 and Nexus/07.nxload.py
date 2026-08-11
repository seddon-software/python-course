'''
The program loads a NeXus (.nxs) file and prints its hierarchical tree structure so you can see how the experimental
data is organised.

# https://nexpy.github.io/nexpy/pythonshell.html#loading-nexus-data
'''

try:
    import nexusformat
except:
    import os
    os.system("python -m pip install nexusformat")

from nexusformat.nexus import *
a=nxload('data/MoKedge_1_15.nxs')
print(a.tree)