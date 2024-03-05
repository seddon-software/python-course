'''
Most programming languages privide an array data structure to contain items.  In Python we have two types
of array: tuples (immutable) and lists (mutable).  List use [] and tuples use ().

In this example we create several lists of integers and compute their average value.
'''


def mean(theList, name):
    total = 0
    for n in theList:
        total = total + n
    average = total / len(theList)
    print(f"average of {name} = {average:.2f}")

mylist = [3, 6, 10, 15, 21, 28, 36]
mean(mylist, "mylist")

mylist2 = [2, 5, 9, 2, 8, 19]
mean(mylist2, "mylist2")

mylist3 = range(1, 20)
mean(mylist3, "mylist3")
