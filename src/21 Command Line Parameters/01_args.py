'''
Introduction
============

When you run any Python app you can pass in parameters from the command line.  For example, by typing
            python 01_args.py red orange yellow green blue indigo violet

in a terminal you will run this program with 7 additional arguments.  However, if you run this program from within 
vscode it will be equivalent to typing
            python 01_args.py

with no additional parameters.  Therefore, if we want to test this program from within vscode, we need to run a
seperate program.  I've created such a program in
            01_runner.py
'''

'''
Command Line Args
=================

Python uses the sys module to input command line arguments.  The arguments are input in the list:
            sys.argv

In this example we enumerate every argument.
'''
import sys

print("Command line parameters")

# simple approach to accessing command line arguments
for i, arg in enumerate(sys.argv):
    print(f"{i}: {arg}")
print()

