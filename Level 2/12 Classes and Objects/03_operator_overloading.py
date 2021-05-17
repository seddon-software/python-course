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
        self = self + other
        return self
    
    # used by print
    def __str__(self):
        return "Time is: " + str(self.hrs) + " hrs," + str(self.min) + " mins"


t1 = Time(5,30)
t2 = Time(3,30)

t3 = t1 + t2
print(t3)

t3 = t1 + 42
print(t3)

t3 = 27 + t1
print(t3)

t1 += t3
print(t3)

t1 += 33
print(t3)


try:
    t3 = t1 + "two mins"
    print(t3)
except Exception as e:
    print(e)    

1
