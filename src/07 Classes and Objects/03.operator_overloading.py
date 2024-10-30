import os; os.system("clear")
'''
Operator Overloading
====================

Like many other languages, Python allows overloading standard operators such that they work with user defined 
classes.  To do this you mush provide special methods for the class.  These special methods (often called 
dunder methods on account of the double set of underscores) are used to overload + - / * etc.

Some common overloads are
            __add__     for +
            __sub__     for -
            __mul__     for *
            __iadd__    for +=
                        
When you overload methods, the object on the left hand side of the operator is special.  This determines the
class where you write the overload.  Thus for
            t1 + t2
            t1 + 42
we need to overload __add__ in the Time class.  However, when we try to add a Time object to an int, as in:
            t3 = 27 + t1
we would have to overload a method in the int class.  Since we don't have access to the int class, Python
provides an alternative: the special method __radd__().  This performs a reverse add (i.e. the arguments are 
swapped such that t1 becomes the left hand operand.  This in turn means we overload __radd__() in the Time class.

Note that += is implemented with __iadd__.  This method has strange semantics:
            t1 += t3

behaves as:
            t1 = t1.__iadd__(t3)

and this in turn implies you must return something from __iadd__(): Python assigns the return value of your
__iadd__ implementation to the object you're "adding to", AFTER the implementation completes.  This rather 
strange semantics is to allow += to make sense with immutable objects (where you return a copy of a new object).
'''

class Time:    
    def __init__(self, hrs, min):
        self.hrs = hrs
        self.min = min

    # rhs must be an int or Time
    def __add__(self, rhs):
        if isinstance(rhs, int): rhs = Time(0, rhs)
        if not isinstance(rhs, Time): raise Exception("Incorrect input type")

        hrs = self.hrs + rhs.hrs
        min = self.min + rhs.min
        if min >= 60:
            hrs = hrs + 1
            min = min - 60
        return Time(hrs, min)
    
    # called if Time is on the rhs
    def __radd__(self, lhs):
        return self + lhs
    
    # called for +=
    def __iadd__(self, other):
        self = self + other     # self now points to a different object (the one returned from __add__)
        return self             # note this is required (see description above)
    
    # used by print
    def __str__(self):
        return "Time is: " + str(self.hrs) + " hrs," + str(self.min) + " mins"


t1 = Time(5,30)
t2 = Time(3,30)

t3 = t1 + t2        # t3 = t1.__add__(t2)
print(t3)

t3 = t1 + 42        # t3 = t1.__add__(42)
print(t3)

t3 = 27 + t1        # t1.__radd__(27)
print(t3)

t1 += t3            # t1 = t1.__iadd__(t3)
print(t1)

t1 += 33            # t1 = t1.__iadd__(33)
print(t1)

try:
    t3 = t1 + "two mins"
    print(t3)
except Exception as e:
    print(e)    


