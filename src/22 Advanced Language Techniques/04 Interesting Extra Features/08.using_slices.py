'''
Using Slices
============
Lists and tuples can be spliced and a number of builtins take slices as parameters, such as range.  You can also
define slices for your own classes by overloading the [] operator using __getitem__ and using the Ellipses 
construct "...".

Most of the example is straightforward, but slicing objects of MyList need some further explanation.  The MyList
class merely wraps a Python list gfor simplicity.  We the define an object "c" of type MyList and set it to:
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

There are 3 cases to consider.  
    1) We might want to take a slice of the list:
                c[10:13]
    2) We might want one element:
                c[-1]
    3) We might want a combination of the above
                c[10:13, ..., 5:7, ..., -2]

In the last case, the 3 dots are a special object called Ellipses.  You can use this object how you like; we
merely treat it as a separator and ignore it in this code.  The "__getitem__()" method does all the hard work
for the above cases.  

Note that we are using itertools to flatten the resulting list in the last case.  The itertools method only 
works on 2D arrays so we have to be careful when processing "-2" and wrap it in a list inside the list of results.
'''

import itertools

debug = True
print(...)
class MyList:
    def set(self, theList):
        self.theList = theList
        
    def __getitem__(self, items):
        if debug: print(f"DEBUG: {items}")
        if isinstance(items, int): return self.theList[items]
        if isinstance(items, slice):        # items = only one slice 
            theSlice = items
            return self.theList[theSlice]
        else:                               # items = mixture of slices and Ellipses
            result = []
            for item in items:           # process each slice and ignore the Ellipses
                if debug: print(f"DEBUG: next item = {item}")
                # ignore Ellipses (...)
                if item == Ellipsis: continue
                if isinstance(self.theList[item], int):  # single ints need to be in a list
                    result.append([self.theList[item]])
                else:
                    result.append(self.theList[item])
            # use itertools to flatten the list
            flattenedList = list(itertools.chain.from_iterable(result))
            return flattenedList

# define slices
mySlice = slice(3,20,2)
print(mySlice)

# use a slice on a list
myList = list(range(100))
result = myList[mySlice]        # equivalent to result = myList[3, 20, 2]
print(result)
print(list(range(10, 30)))
# define an instance of a class supporting []
c = MyList()
c.set(list(range(10, 30)))
print(c[-1])
print((c[10:13]))
print((c[10:13, ..., 5:7, ..., -2]))


