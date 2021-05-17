"""
How do you find the intersection of 2 lists (i.e. those 
elements common to both lists)?
"""


list1 = [ 1, 3, 5, 7, 5, 4, 3, 2, 1 ]
list2 = [ 2, 4, 6, 8, 6, 4, 3, 2, 1 ]

set1 = set(list1)
set2 = set(list2)
common = set1.intersection(set2)
newList = list(common)
print(newList)
