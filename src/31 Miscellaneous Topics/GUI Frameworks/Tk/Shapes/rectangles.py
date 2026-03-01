height = 6.8
width = 3.5

########################################
import tkinter as tk
import numpy as np
from functools import partial

scale = .02
height = height/scale
width = width/scale
w = 600
margin = 10
xLeft = 100
yTop = 100
xRight = xLeft + width
yBottom = yTop + height
sideText = (xLeft - margin, (yTop + yBottom)/2)
baseText = ((xLeft + xRight)/2, yBottom+margin)

slot1 = 0.3*w
slot2 = 0.45*w
slot3 = 0.6*w
slot4 = 0.8*w

def main():
    def printArea(height, width):
        area = height * width
        canvas.create_text(slot2, w-0.5*margin, text=f"{area:.2f}")
    def printPerimeter(height, width):
        perimeter = 2*(height + width)
        canvas.create_text(slot4, w-0.5*margin, text=f"{perimeter:.2f}")
    
    root = tk.Tk()
    root.title("rectangles")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)

    points = (
        (xLeft, yTop),
        (xLeft, yBottom),
        (xRight, yBottom),
        (xRight, yTop)
    )
    canvas.create_polygon(*points, fill='yellow')
    canvas.create_text(*sideText, text=f"{height*scale:.1f}")
    canvas.create_text(*baseText, text=f"{width*scale:.1f}")
    pfn1 = partial(printArea, height*scale, width*scale)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(x=slot1, y=w-2*margin)
    pfn2 = partial(printPerimeter, height*scale, width*scale)
    button = tk.Button(canvas, text="Perimeter", command=pfn2)
    button.place(x=slot3, y=w-2*margin)
    canvas.pack()

    root.mainloop()


main()

