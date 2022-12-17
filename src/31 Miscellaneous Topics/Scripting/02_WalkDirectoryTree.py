############################################################
#
#    walk directory tree
#
############################################################

import os, distutils.sysconfig

sitePackages = distutils.sysconfig.get_python_lib()

for root, dirs, files in os.walk(sitePackages):
    print(root)                          # parent directory
    print("\tSubdirectories: ",dirs)     # subdirectories
    print("\tFiles", files)              # files in parent directory

1
