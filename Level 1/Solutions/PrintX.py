'''
Draw large X on the terminal
Ask user for the size of the figure as an odd number of lines
'''

def drawTopOfX(size):
    for n in range(size):
        leftMargin = n
        rightMargin = 2*(size-leftMargin)-1
        drawSpaces(leftMargin)
        print("╲", end="")
        drawSpaces(rightMargin)
        print("╱")

def drawCrossover(size):
    leftMargin = size
    drawSpaces(leftMargin)
    print("╳")
    pass

def drawBottomOfX(size):
    for n in range(size):
        leftMargin = size - n - 1
        rightMargin = 2*(size-leftMargin)-1
        drawSpaces(leftMargin)
        print("╱", end="")
        drawSpaces(rightMargin)
        print("╲")

def getHalfSizeOfX():
    lines = int(input("How many lines tall will your X be (odd number please)? "))
    if lines > 13: raise Exception("Too many lines")
    if lines < 0: raise Exception("At least one line please")
    if lines%2 == 0: raise Exception("Please enter an odd number of lines")
    halfSize = (lines - 1) // 2
    return halfSize

def drawSpaces(n):
    print(" "*n, end="")

try:
    halfSize = getHalfSizeOfX()
    drawTopOfX(halfSize)
    drawCrossover(halfSize)
    drawBottomOfX(halfSize)
except Exception as e:
    print(f"*** {e} ***")

'''

╲       ╱
 ╲     ╱
  ╲   ╱
   ╲ ╱
    ╳
   ╱ ╲
  ╱   ╲
 ╱     ╲
╱       ╲
'''