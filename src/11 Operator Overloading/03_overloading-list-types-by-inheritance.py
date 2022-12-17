############################################################
#
#    overloading-list-types-by-inheritance.py
#
############################################################

# With sorted list, using inheritance can be problematical, 
# because you need to override all methods in super class 
# that require sorting (we've only looked at __iadd__)

# sorted list
class MyList(list):
    def __init__(self, *args):
        self.extend(args)
        self.sort()
        
    def __iadd__(self, *args):
        self.extend(*args)
        self.sort()
        return self
    
    
myList = MyList(7, 21, 15, 87, 44, 5)
print(myList)
myList += 22, 33, 11, 55
print(myList)
myList.append(5)
print(myList)

a = MyList(1,2)
b = MyList(3,4)
z = a + b
print(z)
 