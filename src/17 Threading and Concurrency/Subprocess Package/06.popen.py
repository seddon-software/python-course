'''
Popen
=====
For more complex tasks you can use "Popen()" instead of "run()".  However, "run()" covers most use cases.  The
"popen()" example is shown here for completeness, but note this example could have been written using "run()".  
'''

import sys
import subprocess

try:
    p = subprocess.Popen(
        'ls -l *.py f1', 
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE, 
        shell=True)
    p.wait()        # wait for child process to terminate
    (out, err) = p.communicate()        
except subprocess.CalledProcessError as e:
    print(e)
    sys.exit()
        
print(f"stdout: \n{out.decode()}")
print(f"stderr: \n{err.decode()}")
