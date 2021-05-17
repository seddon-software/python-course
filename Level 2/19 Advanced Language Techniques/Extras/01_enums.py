# define symbols names
MON, TUE, WED, THU, FRI, SAT, SUN = list(range(7))
# use as enum

print(WED)

def isWeekend(day):
    if day in (SAT, SUN):
        return True
    else:
        return False
        
if isWeekend(MON): print("weekend")
if isWeekend(TUE): print("weekend")
if isWeekend(WED): print("weekend")
if isWeekend(THU): print("weekend")
if isWeekend(FRI): print("weekend")
if isWeekend(SAT): print("weekend")
if isWeekend(SUN): print("weekend")
