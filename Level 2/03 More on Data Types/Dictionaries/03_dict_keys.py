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

# convert to a list
keys_list = list(keys_view)
print(keys_list)

# modify dictionary
salary['jim'] = 63000
salary.pop('tim')

# see if the view changed
print(keys_view)
