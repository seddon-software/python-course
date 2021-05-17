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

    # cast operator
    def __int__(self):
        return self.hrs * 60 + self.min
    
    # used by print
    def __str__(self):
        return "Time is: " + str(self.hrs) + " hrs," + str(self.min) + " mins"

t = Time(7, 10)
n = int(t)
print(n)
