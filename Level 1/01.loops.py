'''
This program uses loops to print mathematical tables.  For example:

        5 x 8 = 40
        6 x 8 = 48
        7 x 8 = 56
        ...
'''

mylist = [0]*30
print(mylist)
n = int(input("Enter a number: "))
print(f"About to print {n} times table")

for x in range(1, 13):
    print(f"{x:2} x {n} = {x * n}")
print()



