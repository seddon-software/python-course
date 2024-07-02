'''
Subprocess Call
===============
The subprocess package is similar to the multiprocessing package in that it allows communication between
processes.  With the subprocess package communication is always between a parent and its child process.

In this example we run a simple Linux command in a child process; the child runs independently of the parent and
doesn't communicate with the parent.  In later examples we will see how to send information back from the child 
to the parent.
'''

import subprocess

print("using call")
print("==========")
subprocess.call(["ls", "-a", "-l"])
print("\n\nusing call with split")
print("=====================")
# or use split
subprocess.call("ls -a -l".split())


