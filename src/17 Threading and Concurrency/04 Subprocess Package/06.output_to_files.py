'''
Output to Files
===============
The "run()" method can also redirect stdout and stderr to different files as shown in this example.
If you want to combine stdout and stderr in the same file set stderr=subprocess.STDOUT; stdout will receive the
combined output and stderr will be set to None.

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