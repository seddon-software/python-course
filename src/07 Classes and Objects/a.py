class Time:
    def __init__(self, h=0, m=0):
#        self.__dict__['h'] = h
        self.hrs = h
        self.min = m

    def __radd__(self, lhs):
        return self + lhs
    
    def __add__(self, rhs):
        if isinstance(rhs, int): rhs = Time(0, rhs)
        if not isinstance(rhs, Time): raise Exception("Incorrect input type")

        result = Time()
        result.hrs = self.hrs + rhs.hrs
        result.min = self.min +rhs.min
        if result.min >= 60:
            result.hrs += 1
            result.min -= 60
        return result
    
    def __str__(self):
        return f"{self.hrs}:{self.min}"


t1 = Time(3, 45)
t2 = Time(2, 40)
t = t1 + 25         # t = t1.__add__(25)
print(t)            # t.__str__()
t = 50 + t1         # t = t1.__radd__(50)
print(t)            # t.__str__()
t = t1 + t2
# t = t1.__add__(t2)
pass


