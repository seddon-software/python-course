'''
Sorted (builtin function)
=========================

Here we examine sorting lists and dictionaries.  Technically speaking we can't sort a dictionary because its
a hash table.  However, we can print out the dictionary in lexical order of the keys. 

The function best suited to this is "sorted".  The sorted function takes two parameters, the first parameter is 
the collection to be sorted and the optional second parameter is a (key) function used for comparing items in the 
collection.  Collections are sorted by a succession of comparisons between pairs of items using a sort algorithm 
(derived from merge sort and insertion sort).   The algorithm was created by Tim Peters in 2002 for use in the 
Python language.

If the key function is omitted, as in
            sorted(weekdays)
standard string comparisons will be used.  When we supply a key function, as in
            sorted(weekdays, key=str.lower)
the key function is applied to each item in the comparison (and normally returns a string).
'''

def basicSorting():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print(sorted(weekdays))

def sortingWithAKey():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print(sorted(weekdays, key=str.lower))

def sortingDictionaryUsingAKeyAndFunction():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    def getSalary(key): 
        return salary[key]
    
    for key in sorted(salary, key=getSalary):
        print(key, salary[key], end=' ')
    print()

def sortingDictionaryUsingAKeyAndLambda():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    for key in sorted(salary, key=lambda key:salary[key]):
        print(key, salary[key], end=' ')
    print()
    
def usingACompareFunction():
    def rank(card):
        pip = card[0]
        suit = card[1]
        suits = "CDHS"
        return suits.find(suit) * 13 + pip
    print(sorted([(8,'H'), (5,'H'), (2,'S'), (4,'D'), (7,'D'), (7,'C'), (3,'H')], 
                 key=rank))

####################################################################

basicSorting()
sortingWithAKey()
sortingDictionaryUsingAKeyAndFunction()
sortingDictionaryUsingAKeyAndLambda()
usingACompareFunction()
