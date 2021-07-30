import os, shutil

os.chdir("data")
source = raw_input("Enter source file: ")
target = raw_input("Enter target file: ")

if not os.path.exists(source):
    print "source does not exist"
elif os.path.exists(target):
    print "target would be overwritten"
else:
    shutil.copyfile(source, target)
