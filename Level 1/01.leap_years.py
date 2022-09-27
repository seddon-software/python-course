'''
Tropical Year = 365.252422 days
Gregorian calendar adds 1 day every 4 years
                   adds 1 day every 400 years
which equates to 365 + 1/4 + 1/400 = 365.2525 days

Thus we need leap years every 4th year and every 4th century

Examples:
    2000        is a leap year      (5 * 400)
    2003        is NOT a leap year  (not divisible by 4)
    2024        is a leap year      (506 * 4)
    2100        is NOT a leap year  (divisible by 100)
'''
print("Days in Gregorian Year:", 365 + 1/4 + 1/400)
