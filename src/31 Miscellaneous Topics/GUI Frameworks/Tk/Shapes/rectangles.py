import tkinter as tk
import numpy as np
from functools import partial

scale = .02
w = 600
margin = 10
height = 300
width = 400
xLeft = 100
yTop = 100
xRight = xLeft + width
yBottom = yTop + height
sideText = (xLeft - margin, (yTop + yBottom)/2)
baseText = ((xLeft + xRight)/2, yBottom+margin)

def main():
    def printAnswer(height, width):
        area = height * width
        canvas.create_text(0.7*w, w-margin, text=f"{area:.2f}")
    
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
    canvas.create_text(*sideText, text=f"{height*scale}")
    canvas.create_text(*baseText, text=f"{width*scale}")
    fn = partial(printAnswer, height*scale, width*scale)
    button = tk.Button(canvas, text="Answer", command=fn)
    button.place(x=0.3*w, y=w-2*margin)
    canvas.pack()

    root.mainloop()


main()

