'''
Converting a File to a Dictionary
=================================

If we have a file containing information of the form of key value pairs, we can read the file into a dictionary.
Because a dictionary is hashed, we can then retreive information about indivial keys in an efficient manner.

The example file contains international phone codes.  The first field on each line is the phone code which we
will use as the value in the dictionary.  The rest of the line will be the state, city or region and this will 
become the key.

I've added a trace to make the code more obvious, but it produces a lot of output.  Switch the trace to False
to get succint output.
'''

from pprint import pprint
trace = False
# trace = True      # this produces a lot of output

def Print(item):
    if item is dict and trace: pprint(item)
    if trace: print(item)

# dictionaries can't be sorted, but we can print out
# key value pairs in lexical order (see previous example)

# 1. Read in dictionary from file
phones = {}
try:
    f = open("data/codes.txt", "r")
    for line in f:
        Print(f"current line: {line}")
        strippedLine = line.rstrip().split(' ')  # split string on spaces
        Print(f"current line as list (stripped): {strippedLine}")
        value = strippedLine[0]  # this is the area code
        key = " ".join(strippedLine[1:]) # this is the region (join list items using a space)
        Print(f"key={key}, value={value}")
        phones[key] = value
        Print(f"Current state of dictionary:")
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
key = "District of Columbia"    
print(f"code for {key} = {phones[key]}")
