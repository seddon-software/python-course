'''
DataClasses
===========

When you create a class, chances are that you want to add a number of standard dunder methods.  The @dataclass
decorator does this for you automatically.  This results in cleaner code whilst still retaining flexibility.
This idea was probably inspired by the Scala programming language.

The decorator requires the use of anotations so that it can generate the correct dunder methods, automatically 
adding generated special methods such as __init__() , __repr__() and __eq__() to user-defined classes.
'''

from dataclasses import dataclass
import inspect

def printList(theList):
    for item in theList:
        print(item)
    print()

@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=False)
class Date:
    # note annotations are reqired
    year: int
    month: int
    day: int

d1 = Date(1984, 1, 1)
d2 = Date(1987, 4, 7)
d3 = Date(2022, 12, 30)
d4 = Date(1987, 5, 1)
d5 = Date(2022, 12, 25)

# use __repr__
dates = [d1, d2, d3, d4, d5]
for d in dates:
    print(d)
print()

# use order
for d in sorted(dates):
    print(d)
print()

# add a day
for d in dates:
    d.day += 1
print()

for d in dates:
    print(d)
print()

# find all methods in class
method_list = [attribute for attribute in dir(Date) if callable(getattr(Date, attribute))]
print(method_list)
