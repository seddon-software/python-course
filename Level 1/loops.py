'''
This program prints tables.  For example:

        5 x 8 = 40
        6 x 8 = 48
        ...
'''

mylist = [0]*30
print(mylist)
n = int(input("Enter a number: "))
print(type(n))

for x in range(1, 13):
    print(f"{x:2} x {n} = {x * n}")
print()



