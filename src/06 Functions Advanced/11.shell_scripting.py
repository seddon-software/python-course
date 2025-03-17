#! /usr/bin/env python
'''
Shell scripts can be run directly from the subprocess module.  Using shell=True allows for 
wildcards like '*' to be used in the script
'''

import subprocess
command = """
echo one
echo two
cd
pwd
date
ls -l
"""

subprocess.run(command, shell = True, executable="/bin/bash")
