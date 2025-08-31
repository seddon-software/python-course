'''
list (mutable)
==============
Lists are mutable arrays.  Index starts at 0 and define and access with []. 

tuple (immutable)
=================
Tuples are immutable arrays.  Index starts at 0 and define and access with []. 
Note that tuples wth a single item have to be defined with a comma to avoid confusion with the expression:
            x2 = (1)
'''

# define several lists and tuples
emptyList = []
emptyTuple = ()
oneEntryTuple = (99,)           # note the comma
mixedTuple = [1, "mixed", 2, 'list']    # you can mix types
twoDimensionalList = [[10,1],[20,21],[30,31,32,33]]       # ragged array

# access elements of 2D list
print(f"{twoDimensionalList[2][3]}")

