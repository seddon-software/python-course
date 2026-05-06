# https://nexpy.github.io/nexpy/pythonshell.html#loading-nexus-data

from nexusformat.nexus import *
a=nxload('data/MoKedge_1_15.nxs')
print(a.tree)