############################################################
#
#    Dates and Times
#
############################################################

import time
import datetime

# localtime returns a 9-tuple
t = time.localtime()
print("tm_hour =", t.tm_hour)
print("tm_isdst =", t.tm_isdst)
print("tm_mday =", t.tm_mday)
print("tm_min =", t.tm_min)
print("tm_mon =", t.tm_mon)
print("tm_sec =", t.tm_sec)
print("tm_wday =", t.tm_wday)
print("tm_yday =", t.tm_yday)
print("tm_year =", t.tm_year)
print()

today = datetime.date.today()
print("today.day =", today.day)
print("today.month =", today.month)
print("today.year =", today.year)
print()

# timetuple returns a 9-tuple
t = today.timetuple()
print(t)

# setup a 9-tuple
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
# mktime converts to seconds
t = time.mktime(t)
print(t)

# formatted time
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))
