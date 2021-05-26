class Time:
    def __init__(self, h, m):
        self.hrs = h
        self.min = m
    def __add__(self, rhs):
        result = Time(0, 0)
        result.hrs = self.hrs + rhs.hrs
        result.min = self.min + rhs.min
        if result.min >= 60:
            result.min -= 60
            result.hrs += 1
        return result

t1 = Time(4, 40)
t2 = Time(3, 25)
result = t1 + t2
print(result.__dict__)
# result = t1.__add__(t2)
# result = Time.__add__(t1, t2)

