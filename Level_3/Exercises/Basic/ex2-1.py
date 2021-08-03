"""
Write a program that inputs a 4 digit year and then 
calculates whether or not it is a leap year.
"""

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2021
if isLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

year = 2024
if isLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

year = 2100
if isLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

year = 2000
if isLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

