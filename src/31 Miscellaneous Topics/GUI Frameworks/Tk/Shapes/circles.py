import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial

scale = .02
w = 600
margin = 10
radius = w/2
arc = 225

baseRadiusText = (0.75*w-margin, 0.50*w+2*margin)
wx = (w+radius*np.cos(arc*π/180))/2
wy = (w-radius*np.sin(arc*π/180))/2
radiusText = (wx, wy)

arcText = np.array((w/2+2*margin, w/2-margin))
answerText = (0.7*w, w-margin)

def main():
    def printAnswer(arc):
        area = π * (radius*scale)**2 * arc / 360
        print(area)
        canvas.create_text(*answerText, text=f"{area:.2f}")
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
    fn = partial(printAnswer, arc)
    button = tk.Button(canvas, text="Answer", command=fn)
    button.place(x=0.3*w, y=w-2*margin)
    canvas.pack()

    root.mainloop()

main()

