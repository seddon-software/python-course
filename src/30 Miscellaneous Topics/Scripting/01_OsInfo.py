############################################################
#
#    search directory tree
#
############################################################

import os

# print OS name, environment variables
print("O/S= ", os.name)
print("Environment variables= ", os.environ)
print("PATH= ", os.environ["PATH"])

# change directory and print CWD
os.chdir("..")
print("CWD= ", os.getcwd())

# check info on a file
if os.path.exists("myfile.txt"): print("'myfile.txt' exists")
if os.path.isfile("myfile.txt"): print("'myfile.txt' exists and is not a directory")
if os.path.isdir("d1"): print("'d1' is a directory")
if os.path.isabs("/home/d1/myfile.txt"): print("'/home/d1/myfile.txt' is an absolute path")


