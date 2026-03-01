height = 5.2
width = 8.3

####################################################
import tkinter as tk
import numpy as np
from functools import partial

scale = .02
height = height/scale
width = width/scale
w = 600
slot1 = 0.3*w
slot2 = 0.45*w
margin = 10
topY = 100
baseY = topY + height
topX = 400
baseX1 = 100
baseX2 = baseX1 + width
middleText = (topX, baseX1 + width/2)
baseText = ((baseX2 + baseX1)/2, baseY+margin)

def main():
    def printArea(height, width):
        area = height * width * scale**2 / 2
        canvas.create_text(slot2, w-0.5*margin, text=f"{area:.2f}")

    root = tk.Tk()
    root.title("triangles")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)

    points = (
        (baseX1, baseY),
        (baseX2, baseY),
        (topX, topY)
    )
    canvas.create_polygon(*points, fill='cyan')
    canvas.create_line(topX, topY, topX, baseY, dash=(10,10))
    canvas.create_text(*middleText, text=f"{height*scale}")
    canvas.create_text(*baseText, text=f"{width*scale}")
    pfn1 = partial(printArea, height, width)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(x=slot1, y=w-2*margin)
    canvas.pack()

    root.mainloop()


main()

