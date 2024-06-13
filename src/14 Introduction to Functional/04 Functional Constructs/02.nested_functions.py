'''
Nested Functions
================

Here is an example of using closures in the nested functions "getSum()" and "getLength()".  The parent function 
"getStats()" calls these functions which operate on "myList".  The closure avoids repeating passing parameters 
to the nested functions.  Nested functions with closures make code simpler and allow us to define function close 
to the point where they are used.  This is superior to using global functions that could be defined a long way 
away from where they are used (or even in a different file).
'''

def getStats(myList):
    def getSum():       # no need to pass myList as a parameter
        total = 0
        for i in myList:
            total += i
        return total
    def getLength():
        return len(myList)
    
    print(f"sum of list = {getSum()}")
    print(f"length of list = {getLength()}")

getStats(list(range(10)));
