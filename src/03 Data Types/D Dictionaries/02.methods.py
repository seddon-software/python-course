'''
Dictionary Methods
==================
Dictionaries support a number of methods (operations).  Common operations are shown in the examples below.

Note that, starting with Python 3.7, the standard guarantees that dictionaries preserve the order in which 
key, value pairs were inserted.
'''

# set up a dictionary
salary = {
 		  "zak":   34000, 
          "sara":  27000,
          "pedro": 52000,
          "rocco": 12500,
          "zoe":   66000
         }
print(salary)

# update an existing key in dictionary
salary["sara"] = 28000
salary["sara"] = None       # use None if value unknown
print(salary)  # preserves order in which key, value pairs were inserted (standard behaviour in Python 3.7+)

# add a new key, value pair (same syntax as updating)
salary["george"] = 137000
print(salary)

# read and write entries
salary["pedro"] = 53000
print(salary["pedro"])

# print all the keys
for key in salary.keys():
    print(key, end=' ')
print()

# print all the values
for value in salary.values():
    print(value, end=' ')
print()

# print all <key,value> pairs
for key, value in salary.items():
    print(key, value)

# enumerate all key value pairs (includes loop count)
for i, (key, value) in enumerate(salary.items()):
    print(i, key, value)

# check if key in dictionary
if "george" in salary: print("george is in dictionary")
if "sara" in salary: print("sara is in dictionary")
if "tom" not in salary: print("tom is NOT in dictionary")

# delete keys using del or pop
del salary["zak"]           # nothing returned (discouraged)
value = salary.pop("sara")  # returns value of key that has been deleted


