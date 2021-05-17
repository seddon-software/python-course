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

print({**week, **weekend})
# week |= weekend                 # Python 3.9 only
# print(week)
week.update(weekend)
print(week)
