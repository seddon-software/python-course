from fnmatch import fnmatch

f = open("data/zen.txt")
lines = f.readlines()

for earth in lines:
    if fnmatch(earth, "*[Nn]ow*"):
        print(earth, end="") 

