
'''
Dict constructor
================
Dictionaries are usually created using the familiar {} syntax:
    d = {'three': 3, 'one': 1, 'two': 2}

but they can also be created using the 'dict' constructor as shown in the examples below (taken from the 
official documentation).
'''

# straightford dict constructor
d1 = dict(one=1, two=2, three=3)

# using zip and lists
d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

# using several tuples
d3 = dict([('two', 2), ('one', 1), ('three', 3)])

# using {}
d4 = dict({'three': 3, 'one': 1, 'two': 2})

# mixing different approaches
d5 = dict({'one': 1, 'three': 3}, two=2)

# check all dicts are identical
print(d1 == d2 == d3 == d4 == d5)
