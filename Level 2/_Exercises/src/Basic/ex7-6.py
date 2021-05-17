'''
Write a program that emulates the grep command with a pattern such as:
    grep [Nn]ow data/zen.txt
'''

import os
from fnmatch import fnmatch

os.system("grep [Nn]ow data/zen.txt")
f = open("data/zen.txt")
lines = f.readlines()

print("===================")

for earth in lines:
    if fnmatch(earth, "*[Nn]ow*"):
        print(earth, end="") 
