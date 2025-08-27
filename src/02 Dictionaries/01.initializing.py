'''
Creating Dictionaries
=====================

Dictionaries are collections of key, value pairs of items.  The key must be immutable, but the value can be
mutable or immutable.  Dictionaries are often called hash tables or associative arrays.

Note that Python keeps track of the insertion order with a hidden backing array.
'''

# normal way to initialize a dictionary
salary = {
 		  "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

# entries are printed in insertion order
print(salary)
