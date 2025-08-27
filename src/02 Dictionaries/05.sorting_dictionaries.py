'''
Sorting Dictionaries
====================

Dictionaries do not define an order, however since Python 3.7 dictionaries have a backing array which contains 
keys in the order in which entries were added to the dictionary.  So if you iterate through a dictionary you
will notice key, value parts are in insertion order.

If you want to sort a dictionary in some logical order other than insertion order (e.g. lexical order), you need 
to create an additional list containing the keys which you then sort.  Note that, because a dict is hashed,
retreiving values is a very fast operation.

If you want to use a different criteria for sorting the dictionary use the "sorted" built in function. This 
takes a comparator function that returns something other than the key which will then be sorted (in our case the 
value of the key). 
'''

# set up a dictionary
salary = {
          "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

# extract the keys and sort them
mylist = list(salary.keys())
mylist.sort()

print("Dictionary in key lexical order:")
# go back to the dictionary and pull out values in lexical order
for key in mylist:
    print(f"{key:<6s}{salary[key]:6}")
print()

# don't do this (why?)
sortedlList = list(salary.keys()).sort()
print(sortedlList)

# use sorted to sort dictionary in a different order (by value)
def comparator(key):
    return salary[key]      # this will be used as the sort value

print("Dictionary in value numerical order:")
for key in sorted(salary, key=comparator, reverse=False):
    print(f"{key:<6s}{salary[key]:6}")
print()

print("Dictionary in reverse value numerical order:")
for key in sorted(salary, key=comparator, reverse=True):
    print(f"{key:<6s}{salary[key]:6}")
print()
