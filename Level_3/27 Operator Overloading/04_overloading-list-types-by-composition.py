############################################################
#
#    overloading-list-types-by-composition.py
#
############################################################

# using composition is superior to using inheritance, because we can
# decide which methods to override

# sorted list
class MyList(object):
    def __init__(self, *args):
        self.theList = list(args)
        self.theList.sort()
        
    def __iadd__(self, *args):
        self.theList.extend(*args)
        self.theList.sort()
        return self
    
    def __str__(self):
        return self.theList.__str__()
    
myList = MyList(7, 21, 15, 87, 44, 5)
print(myList)
myList += 22, 33, 11, 55
print(myList)

1