"""
Using a variation of the above program, calculate the 
number of days in the inclusive date range 
'1st January 2000' to '31st December 2999'.
"""

def daysInYear(year):
    days = 365
    if year %   4 == 0: days = 366
    if year % 100 == 0: days = 365
    if year % 400 == 0: days = 366
    return days

totalDays = 0
for year in range(2000, 3000):
    totalDays += daysInYear(year)

print(totalDays)

