import collections

# form a dictionary that contains count of occurances of items in source data

s = 'mississippi'
sourceData = ('red', 'blue', 'red', 'green', 'white', 'blue', 'white', 'red')

myDictionary = collections.defaultdict(lambda : 0) # factory function always returns 0

for key in sourceData:
    myDictionary[key] += 1

print(list(myDictionary.items()))


1
