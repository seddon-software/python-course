'''
inspect files
=============
'''

import subprocess, os

print("see what files are present after build")
subprocess.call("tree ..".split())
