week = {
        'mon': 'Monday', 
        'tue': 'Tuesday',
        'wed': 'Wednesday',
        'thu': 'Thursday',
        'fri': 'Friday'
        }
weekend = {
           'sat': 'Saturday',
           'sun': 'Sunday'
           }

# 1. using kwargs
print({**week, **weekend})

# 2. Python 3.9 method
weekBackup = week.copy()
week |= weekend                 # Python 3.9 only
print(week)

# 3. using the update method
weak = weekBackup.copy()
week.update(weekend)
print(week)


