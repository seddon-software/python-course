import os, shutil
import setPath

os.chdir("../src")

# create source distro
os.system("python setup.py sdist --formats=zip")

# copy to local repo
shutil.copy("dist/mymodule-1.0.zip", "../server/repo")
print("\n", "mymodule-1.0.zip", "copied to local repo")