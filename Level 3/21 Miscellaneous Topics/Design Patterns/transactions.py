############################################################
#
#    Transactions
#
############################################################


class Point:
    def __init__(self, x0 = 0, y0 = 0):
        self.x = x0
        self.y = y0
    
    # copy CTOR in C++
    def Copy(self):
        return Point(self.x, self.y)

    # operator= in C++
    def Reset(self, p):
        self.x = p.x
        self.y = p.y
    
    def MoveBy(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.x > 150: raise Exception("x too big")

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"
        
class Transaction:
    def __init__(self):
        self.participants = []
        self.snapshot = []
        
    def Join(self, p):
        self.participants.append(p)
        
    def Begin(self):
        # save copies in snapshot
        for participant in self.participants:
            self.snapshot.append(participant.Copy())

    def Commit(self):
        del self.snapshot[:]
        
    def Rollback(self):
        # restore copies from snapshot
        for participant, point in zip(self.participants, self.snapshot):
            participant.Reset(point)
        del self.snapshot[:]


p1 = Point(10, 10)
p2 = Point(20, 10)
p3 = Point(30, 10)
for p in (p1, p2, p3):
    print(p, end=' ') 
print(": Start")

t = Transaction()

t.Join(p1)
t.Join(p2)
t.Join(p3)

try:
    # these operations will succeed
    t.Begin()
    p1.MoveBy(30, 10)
    p2.MoveBy(30, 10)
    p3.MoveBy(30, 10)
    t.Commit()
except Exception as e:
    t.Rollback()

for p in (p1, p2, p3):
    print(p, end=' ')
print(": Commit")

try:
    # these operations will fail
    t.Begin()
    p1.MoveBy(99, 88)
    p2.MoveBy(99, 88)
    p3.MoveBy(99, 88)   # raises exception
    t.Commit()
except Exception as e:
    t.Rollback();

for p in (p1, p2, p3):
    print(p, end=' ') 
print(": Rollback")

