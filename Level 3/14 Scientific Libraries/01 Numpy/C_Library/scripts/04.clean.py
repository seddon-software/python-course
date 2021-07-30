import os

os.chdir("../src")
os.system("which python")
os.system("python setup.py clean --all")
print("staging area cleaned")


