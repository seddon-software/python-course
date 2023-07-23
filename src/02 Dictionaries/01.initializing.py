'''
Creating Dictionaries
=====================

Dictionaries are collections of key, value pairs of items.  The key must be immutable, but the value can be
mutable or immutable.  Dictionaries are often called hash tables or associative arrays.
'''

# normal way to initialize a dictionary
salary1 = {
 		  "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

# alternate way to initialize a dictionary
salary2 = dict(             # this notation is uncommon 
            john = 34000, 
            sara = 27000, 
            pedro = 52000,
            tim = 12500,
            zoe = 66000
            )
print(salary1)
print(salary2)
