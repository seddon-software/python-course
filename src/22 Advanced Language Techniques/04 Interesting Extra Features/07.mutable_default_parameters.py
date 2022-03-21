'''
Mutable Default Parameters
==========================
Using mutable default parameters for a function is not a good idea.  Consider the example below where we define
item and extra as defaults.  Because item is an int and its immutable this is OK, but extra is mutable and gets
attached to the function object by closure.  Now when we call
            Grow(theList)

the default parameters, item and extra, are used in the code.  Then when we execute
            extra.append(item)

the default parameter gets the item appended to it.  This means the default parameter, extra, is not constant
and it gets longer and longer with each call and is never empty after the first call - not intuitive!!.  Note 
that extra doesn't get used if you pass all three parameters as in
            Grow(theList, 1, [9, 10])
'''

# avoid using mutable default parameters - not intuitive!!
def Grow(theList, item = 0, extra = []):
    extra.append(item)
    theList.extend(extra)
    print(theList)
    
theList = []

Grow(theList, 1, [9, 10])
Grow(theList)       # extra = [0]
Grow(theList)       # extra = [0, 0]
Grow(theList)       # extra = [0, 0, 0]
Grow(theList)       # extra = [0, 0, 0, 0]
Grow(theList, 2, [9, 10])
Grow(theList)       # extra = [0, 0, 0, 0, 0]
