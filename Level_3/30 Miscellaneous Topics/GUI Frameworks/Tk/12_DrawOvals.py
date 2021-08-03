############################################################
#
#	Draw Ovals
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Draw Ovals")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    canvas = Canvas(frame, cursor = "crosshair")
    canvas.pack(side = "left", fill = "both", expand = 1)
    
    x1 = 100; y1 = 100
    x2 = 300; y2 = 200
    
    coords = (x1, y1, x2, y2)
    options = {'width':5.0, 'fill':"yellow", 'outline':"blue"}
    oval = canvas.create_oval(coords, **options)


main()









