import collections


def myFactory():
    return 0
    
# create a defaultdict object
mylist = collections.defaultdict(myFactory)

# behaves like a regular dict object ...
mylist['a'] = 100
mylist['b'] = 200
mylist['c'] = 300
print(mylist)

# ... unless key not defined.  In which case factory method is called to supply a value
print(mylist['d'])   # note that dict is updated with default key
print(mylist)


1
