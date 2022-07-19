'''
sets
====

Sets are a mutable collection of items.  It is important to realize that sets do not maintain an order and that
you can't have duplicate items (they are removed automatically).  Sets have very few methods.

FrozenSets are an immutable version of sets.  To create a frozen set you must first create a list, tuple or set.
'''

# sets are mutable
myset = set(("Monday", "Tuesday"))
myset.add("Wednesday")
myset.add("Thursday")
myset.add("Friday")
print(myset)

# check for existance
if "Wednesday" in myset: print("member")
myset.remove("Wednesday")
if "Wednesday" not in myset: print("not a member")

# frozen sets are built from sets, lists or tuples
mylist = 1, 2, 3, 4, 5, 4, 3, 2, 1
bag = frozenset(mylist)     # duplicates will be removed
print(bag)

# frozen sets are immutable
try:
    bag.add(3)      # this will fail
except Exception as e:
    print(e)

myset = set(("Monday", "Tuesday"))


