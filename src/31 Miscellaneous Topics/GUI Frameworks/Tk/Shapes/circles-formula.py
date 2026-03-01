import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial

m = 10
w = 500


def main():
    root = tk.Tk()
    root.title("arcs of circle")
    height = width = 530
    root.geometry(f"1200x600")

    areaCanvas = tk.Canvas(root, width=width, height=height)
    perimeterCanvas = tk.Canvas(root, width=width, height=height)
    r1 = np.array([0, 0, 1, 1])*w/2 + np.array([2,2,2,2])*m
    r2 = np.array([1, 0, 2, 1])*w/2 + np.array([3,2,3,2])*m
    r3 = np.array([0, 1, 1, 2])*w/2 + np.array([2,3,2,3])*m
    r4 = np.array([1, 1, 2, 2])*w/2 + np.array([3,3,3,3])*m
    perimeter = ['πr/2','πr','3πr/2','2πr']
    area = ['πr²/4','πr²/2','3πr²/4','πr²']
    for i, r in enumerate((r1, r2, r3, r4)):
        print(r)
        n = i + 1
        x = (r[0] + r[2])/2
        y = (r[1] + r[3])/2
        if n == 4:
            areaCanvas.create_oval(*r, fill="cyan")
            perimeterCanvas.create_oval(*r, fill="yellow")
        else:
            areaCanvas.create_arc(*r, start=0, extent=90*n, fill="cyan")
            perimeterCanvas.create_arc(*r, start=0, extent=90*n, fill="yellow")
        areaCanvas.create_text(x, y, text=area[i], fill="black", font=("Arial",32))
        perimeterCanvas.create_text(x, y, text=perimeter[i], fill="blue", font=("Arial",32))
    areaCanvas.create_text(350, 7, text="area", fill="black", font=("Arial",16, "bold"))
    perimeterCanvas.create_text(350, 7, text="perimeter", fill="blue", font=("Arial",16, 'bold'))
    areaCanvas.pack(side='left')
    perimeterCanvas.pack(side='right')

    root.mainloop()

main()

