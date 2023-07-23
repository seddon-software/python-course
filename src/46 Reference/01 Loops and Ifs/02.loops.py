'''
Loops
=====
Python has 2 different types of loop: for and while.  Examples are given below.
'''


# use a sequence (tuple)
for i in 1, 2, 3, 4, 5:
    print(i, end=", ")
print()

# use range
for i in range(0, 6):   # note range goes from 0 to 5 inclusive (not to 6)
    print(i, end=", ")
print()

# use while
n = 0
while n < 6:
    print(n, end=", ")
    n += 1
print()

