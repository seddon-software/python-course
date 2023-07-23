'''
dict_keys
=========
In Python 3, some of the dictionary methods have been modified to return dict_key objects as an optimisation.
Calling keys() on a dictionary will return a dictionary view object. It supports operations like membership 
test and iteration, but its contents are not independent of the original dictionary; it is only a view.
'''

# set up a dictionary
salary = {
          "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

# get a view of keys (iterable)
keys_view = salary.keys()
print(type(keys_view))

# print the view
print(keys_view)

# convert to a list of keys
keys_list = list(keys_view)
print(keys_list)

# modify dictionary
salary['jim'] = 63000
salary.pop('tim')

# see if the view changed (it should)
print(keys_view)
