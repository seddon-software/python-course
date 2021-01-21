import itertools

# define a class that overloads the [] operator using __getitem__
# and uses the Ellipses construct (...)
class mylist(object):
    def __init__(self, theList):
        self.theList = theList
        
    def __getitem__(self, items):
        if isinstance(items, slice):
            theSlice = items
            return self.theList[theSlice]
        else:
            slices = items
            result = []
            for _slice in slices:
                # ignore Ellipses (...)
                if _slice != Ellipsis:
                    x = self.theList[_slice]
                    if isinstance(x, int):
                        result.append([self.theList[_slice]])
                    else:
                        result.append(self.theList[_slice])
            flattenedList = list(itertools.chain.from_iterable(result))
            return flattenedList

# define slices
mySlice = slice(3,9,2)
print(mySlice)

# define lists
myList = list(range(100))
print((myList[mySlice]))

# define an instance of a class supporting []
c = mylist(list(range(10, 30)))
print((c[10:13]))
print((c[10:13, ..., 5:7, ..., -2]))


