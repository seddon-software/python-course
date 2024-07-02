'''
Using Call from the Shell
=========================
When shell=True, the command is passed to the shell for interpretation of shell wildcards etc. Be careful of 
shell injection when the command accepts input, ref:
            https://www.hackingarticles.in/comprehensive-guide-on-os-command-injection
'''

import subprocess


subprocess.run("ls -l *.py", shell=True)


