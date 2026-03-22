'''
Lists are used everywhere in Python.  Some of the common idioms are shown below.
Note how easy it is to fill a list with the same item repeated as in:
            [100] * 15

The range generator is often used to create a list that contains a sequence.  Note that the range generator creates a range object
(a kind of zipped list) which needs to be cast to a list (unzipped).
'''

# create empty list
myList = []

# append items
myList.append(10)
myList.append(20)
myList.append(30)
print(myList)

# extend the list
anotherList = [40, 50, 60]
myList.extend(anotherList)
print(myList)

# create a list filled with numbers
numbers = [100] * 15    # length 15, contents all 100
print(numbers)

# use range to create a list starting at 10 with increments of 2 up to, but not including 30
sequence = list(range(10, 30, 2))
print(sequence)
