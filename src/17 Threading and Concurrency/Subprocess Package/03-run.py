import subprocess
from subprocess import CalledProcessError

# run() is a replacement for call()
# run() returns a CompletedProcess object instead of the process return code.

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

try:
    r = subprocess.run("ls -l *.py", shell=True, check=True)
    print(type(r), r)
except CalledProcessError as e:
    print(f"Failed: {e}")
    