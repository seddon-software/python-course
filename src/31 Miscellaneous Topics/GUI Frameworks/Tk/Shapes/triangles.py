import tkinter as tk
import numpy as np
from functools import partial

scale = .02
w = 600
margin = 10
topX = 400
baseX1 = 100
baseX2 = 500
topY = 100
baseY = 400
height = (baseY - topY)*scale
width = (baseX2 - baseX1)*scale
middleText = (topX, baseX1 + width/2)
baseText = ((baseX2 + baseX1)/2, baseY+margin)

def main():
    def printAnswer(height, width):
        area = height * width / 2
        canvas.create_text(0.7*w, w-margin, text=f"{area:.2f}")
    
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
    canvas.create_text(*middleText, text=f"{height}")
    canvas.create_text(*baseText, text=f"{width}")
    fn = partial(printAnswer, height, width)
    button = tk.Button(canvas, text="Answer", command=fn)
    button.place(x=0.3*w, y=w-2*margin)
    canvas.pack()

    root.mainloop()


main()

