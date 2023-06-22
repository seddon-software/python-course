'''
In the last example code to compute the average value of the list was repeated 3 times.  In practice
we would rewrite this example using functions to avoid the duplication.
'''

def findAverage(anyList):
    total = 0
    for n in anyList:
        total = total + n
    average = total / len(anyList)
    return average

mylist = [3, 6, 10, 15, 21, 28, 36]
average = findAverage(mylist)
print(f"average of mylist = {average:.2f}")

mylist2 = [2, 5, 9, 2, 8, 19]
average = findAverage(mylist2)
print(f"average of mylist2 = {average:.2f}")

mylist3 = range(1, 20)
average = findAverage(mylist3)
print(f"average of mylist3 = {average:.2f}")
