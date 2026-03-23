'''
Run
===
Python 3.5 added "run".  "run()" is a replacement for "call()"; it returns a "CompletedProcess" object instead 
of the process return code and throws an exception on error.  "run()" also makes it easy to capture stdout and 
stderr from the child process.

"run()" should be used in place of "call()" in all new applications.
'''

import subprocess
from subprocess import CalledProcessError

# run() returns normally if the command completes with a zero exit status
response = subprocess.run("ls -l *.py", shell=True, check=True)
print(f"run() returns an object of type: {type(response)}")
print(response)    
print()

# this checks if the child fails (non-zero exit status), in which case a subprocess.CalledProcessError is raised
try:
    subprocess.run("exit 17", shell=True, check=True)
except CalledProcessError as e:
    print(f"Failed (example 1): {e}")
print()

try:
    subprocess.run("cp f1", shell=True, check=True)
except CalledProcessError as e:
    print(f"Failed (example 2): {e}")
print()

    