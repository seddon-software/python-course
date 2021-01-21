############################################################
#
#    decorators
#
############################################################

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

1






