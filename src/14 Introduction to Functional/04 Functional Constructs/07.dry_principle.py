'''
In this example we take a complicated function and split it into simpler functions. While not strictly currying, it does show the use case for decomposing 
a function that has several responsibilities into several smaller functions that have a single responsibilty (DRY principle - don't repeat yourself).  One 
could argue this leads to simpler coding and greater flexibility as the individual functions can be combined in multiple ways.
'''

import datetime

# this function has 3 responsibilities
def getBoldUsDate():
    # 1. get today's date (UK)
    ukDate = datetime.datetime.now()
    ukDateStr = f"{ukDate.day}/{ukDate.month}/{ukDate.year}"
    # 2. convert to US date
    fields = ukDateStr.split('/')
    usDate = fields[1] + "/" + fields[0] + "/" + fields[2]
    # 3. add bold tags
    boldUsDate = "<b>" + usDate + "</b>"
    return boldUsDate

print(f"without currying: {getBoldUsDate()}")

# split the above function into 3 simpler functions
def bold(fn):
    def decorate():
        # surround with bold tags before calling original function
        return "<b>" + fn() + "</b>"
    return decorate

def us(fn):
    def decorate():
        # swap month and day
        fields = fn().split('/')
        date = fields[1] + "/" + fields[0] + "/" + fields[2]
        return date
    return decorate
    
def getDate():
    now = datetime.datetime.now()
    return "%d/%d/%d" % (now.day, now.month, now.year)

# now use the curried functions      
print(f"date: {getDate()}")
boldUsDate = bold(us(getDate))
boldUkDate = bold(getDate)
print(f"bold-date: {boldUsDate()}")
print(f"bold-us-date: {boldUsDate()}")
