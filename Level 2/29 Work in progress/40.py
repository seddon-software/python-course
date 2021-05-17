import numpy as np

balls = np.empty( (4,8), dtype=int)

for i in range(4):
    for k in range(8):
        balls[i,k] = i #i*8+k


def clockwise(cell):
    balls[cell] = np.roll(balls[cell], 1)
#    print(balls)

def anticlockwise(cell):
    balls[cell] = np.roll(balls[cell], -1)
#    print(balls)

def cycleRight():
    temp = balls[0,0]
    balls[0,0] = balls[0,4]
    balls[0,4] = balls[1,0]
    balls[1,0] = balls[1,4]
    balls[1,4] = balls[2,0]
    balls[2,0] = balls[2,4]
    balls[2,4] = balls[3,0]
    balls[3,0] = balls[3,4]
    balls[3,4] = temp
#    print(balls)    
    
def cycleLeft():
    for i in range(7):
        cycleRight()
#    print(balls)

def L(): 
    cycleLeft()
    cycleLeft()
def R():
    cycleRight()
    cycleRight()
A=anticlockwise
C=clockwise

print(balls)
L()
C(2)
L()
A(1)
R()
C(2)
R()
A(1)
print(balls)
