'''
enums
=====
Python makes it easy to define enumerated types.  Simply define a set of symbols and assign integers to each
symbol.
'''

# define symbols names and assign values
MON, TUE, WED, THU, FRI, SAT, SUN = list(range(7))
# use as enum

print(f"WED has value {WED}")

def check(day):
    if day in (SAT, SUN):
        print("is at weekend")
    else:
        print("is during the week")
        
check(MON)
check(TUE)
check(WED)
check(THU)
check(FRI)
check(SAT)
check(SUN)
