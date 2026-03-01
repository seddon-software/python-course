radius = 3.7           # change this
arc = 90               # change this

#############################################################
import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial

scale = .02
radius = radius/scale
margin = 10
w = int(2 * radius)

slot1 = 0.2*w
slot2 = 0.45*w
slot3 = 0.55*w
slot4 = 0.9*w
π = 3.14
baseRadiusText = (0.75*w-margin, 0.50*w+2*margin)
wx = (w+radius*np.cos(arc*π/180))/2
wy = (w-radius*np.sin(arc*π/180))/2
radiusText = (wx, wy)

arcText = np.array((w/2+2*margin, w/2-margin))
areaText = (slot2, w-0.5*margin)
perimeterText = (slot4, w-0.5*margin)

def main():
    def printArea(arc):
        area = π * (radius*scale)**2 * arc / 360
        print(area)
        canvas.create_text(*areaText, text=f"{area:.3f}")
    def printPerimeter(arc):
        perimeter = 2 * radius*scale + 2 * π * radius*scale * arc / 360
        print(perimeter)
        canvas.create_text(*perimeterText, text=f"{perimeter:.3f}")
    root = tk.Tk()
    root.title("arcs of circle")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)
    arcBoundingRectangle = np.array((margin, margin, margin+w, margin+w))
    canvas.create_arc(*arcBoundingRectangle, start=0, extent=arc, fill="red")
    smallArcBoundingRectangle = np.array((w/2-2*margin, w/2-2*margin, w/2+4*margin, w/2+4*margin))
    canvas.create_arc(*smallArcBoundingRectangle, start=0, extent=arc, fill="cyan")
    canvas.pack()

    canvas.create_text(baseRadiusText, text=f"{radius*scale}")
    canvas.create_text(radiusText, text=f"{radius*scale}")
    canvas.create_text(*arcText, text=f"{arc}")
    pfn1 = partial(printArea, arc)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(x=slot1, y=w-2*margin)
    pfn2 = partial(printPerimeter, arc)
    button = tk.Button(canvas, text="Perimeter", command=pfn2)
    button.place(x=slot3, y=w-2*margin)
    canvas.pack()

    root.mainloop()

main()

