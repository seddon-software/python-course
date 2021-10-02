############################################################
#
#    creating subprocesses
#
############################################################

import subprocess, sys

# Python executable is : sys.executable
args = [sys.executable, "child2.py", "Monday", "Tuesday", "Wednesday"]

# run child process, pass command line and a message and capture stdout
result = subprocess.run(args, 
                        input="This is the parent calling", 
                        stdout=subprocess.PIPE, 
                        universal_newlines=True)
print("Message from child:", result.stdout)



1