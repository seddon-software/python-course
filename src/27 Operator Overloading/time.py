class Time:
    def __init__(self, h = 0, m = 0):
        self.hrs = h
        self.min = m
    def __add__(self, rhs):
        result = Time()
        if isinstance(rhs, int):
            rhs = Time(0, rhs) 
        result.hrs = self.hrs + rhs.hrs
        result.min = self.min + rhs.min
        if result.min >= 60:
            result.min -= 60
            result.hrs += 1
        return result
    def __radd__(self, lhs):
        return self + lhs
    def __str__(self):
        return f"[{self.hrs},{self.min}]"
    def __iadd__(self, rhs):
        self = self + rhs
        return self
t1 = Time(4, 50)
t2 = Time(3, 25)
t1 += t2        # t1 = t1.__iadd__(t2)
print(t1)
t = t1 + 20
print(t)
t = 20 + t1     # t = t1.__radd__(20)
print(t)
t = t1.__add__(t2)
t = t1 + t2     # t = t1.__add__(t2)
print(t)
pass