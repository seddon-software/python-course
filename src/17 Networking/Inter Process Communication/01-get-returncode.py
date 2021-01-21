############################################################
#
#    creating subprocesses
#
############################################################

import subprocess
import sys

# Python executable is : sys.executable
# run child process and check return code
result = subprocess.run([sys.executable, "child1.py"])
print("Child returned:", result.returncode)

