'''
Output to Files
===============
The "run()" method can also redirect stdout and stderr to files as shown in this example.
'''

import subprocess
import sys, os

# create two files to hold the output and errors, respectively
# and use shell to interpret wildcards
with open('out.txt','w') as outFile:
    with open('err.txt','w') as errorFile:
        subprocess.run("ls -lha *.py f1", shell=True, stdout=outFile, stderr=errorFile)

os.system("cat out.txt")
os.system("cat err.txt")
