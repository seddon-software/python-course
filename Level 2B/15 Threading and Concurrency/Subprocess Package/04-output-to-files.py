import subprocess
import sys, os

# create two files to hold the output and errors, respectively
# and use shell to interpret wildcards
with open('out.txt','w') as out:
    with open('err.txt','w') as err:
        subprocess.run("ls -lha *.py f1", shell=True, stdout=out, stderr=err)

os.system("cat out.txt")
os.system("cat err.txt")
