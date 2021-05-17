f = open("../data/salaries.txt")

mylist = f.readlines() # returns a list
mydict = {}

for line in mylist:
    key, value = line.split(",")
    mydict[key] = int(value)

print(mydict)
print((mydict["Bill"]))


    