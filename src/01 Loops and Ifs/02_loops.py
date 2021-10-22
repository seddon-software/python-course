import os; os.system("clear")

# use a sequence (tuple)
for i in 1, 2, 3, 4, 5:
    print(i, end=", ")
print()

# use range
for i in range(1, 5+1):   # note 6 is not part of the loop
    print(i, end=", ")
print()

# use while
while i < 6:
    print(i, end=", ")
    i += 1
print()

