'''
Converting a File to a Dictionary
=================================

If we have a file containing information of the form of key value pairs, we can read the file into a dictionary.
Because a dictionary is hashed, we can then retreive information about indivial keys in an efficient manner.
'''

trace = True

def Print(item):
    if trace: print(item)

# dictionaries can't be sorted, but we can print out
# key value pairs in lexical order (see previous example)

# 1. Read in dictionary from file
phones = {}
try:
    f = open("data/codes.txt", "r")
    for line in f:
        Print(f"current line: {line}")
        strippedLine = line.rstrip().split(' ')
        Print(f"current line as list (stripped): {strippedLine}")
        value = theList[0]
        x = theList[1:]
        Print(x)
        y = "".join(x)
        Print(y)
        key = " ".join(theList[1:])
        phones[key] = value
        Print(phones)
except IOError as e:
    print("Reading data from file failed!")
    print(e)
finally: 
    f.close()

# 2. Sort the keys
sortedKeys = list(phones.keys())
sortedKeys.sort()

# 3. Iterate through sorted list
for key in sortedKeys:
    print(key + ":" + phones[key])

# 4. Search for a given value    
print(phones['District of Columbia'])
