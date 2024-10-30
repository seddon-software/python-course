import os; os.system("clear")
'''
Chaining Decorators
===================

Decorators can be combined (chained together).  Here we define "bold()" and "us()" decorators.  These decorators
can be used on their own or in combination:
            @bold
            @us
            def getBoldUsDate():
                return getDate()

In this case:
            getBoldUsDate()

gets translated to 
            us(getBoldUsDate)()
and the second decorator further translates to
            bold(us(getBoldUsDate))
'''

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
    
import datetime
def getDate():
    now = datetime.datetime.now()
    return "%d/%d/%d" % (now.day, now.month, now.year)

@bold
def getBoldDate(): 
    return getDate()

@us
def getUsDate():
    return getDate()

@bold
@us
def getBoldUsDate():
    return getDate()


print("original", getDate())
print("bold    ", getBoldDate())
print("us      ", getUsDate())

#   print(bold(us(getBoldUsDate))())
print("bold+us ", getBoldUsDate())








