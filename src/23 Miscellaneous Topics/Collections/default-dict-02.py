import collections

# form a dictionary that contains list of numbers formed from a list of key value pairs

# set up a sequence of key value pairs for testing
sequence = [('red', 10), ('blue', 22), ('red', 30), ('blue', 44), ('red', 80), ('green', 200)]

# create a defaultdict using the list class as a factory
# if a key is missing list() will be invoked which returns an empty list
myDictionary = collections.defaultdict(list)

# now access our defaultdict for each key, value pair in the original sequence
# since the key doesn't exist in our defaultdict, list() will be called each time
# creating empty values for each key.  We then populate the values using append() 
for key, value in sequence:
    myDictionary[key].append(value)


print(list(myDictionary.items()))


1
