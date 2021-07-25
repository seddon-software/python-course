import os

# add parent directory to PATH environment variable
os.chdir("..")
os.environ["PATH"] = os.getcwd() + ";" + os.environ["PATH"]

# print out each component in the path
path_as_string = os.environ["PATH"]
path_as_list = path_as_string.split(":")
for entry in path_as_list:
    print(entry)


