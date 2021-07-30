############################################################
#
#	Mouse Events
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Mouse Events")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def callback(event):
    if(event.num == 1): callback.label.configure(text = "Left button pressed")
    if(event.num == 2): callback.label.configure(text = "Middle button pressed")
    if(event.num == 3): callback.label.configure(text = "Right button pressed")


def draw(frame):
    label = Label(frame, text = "Press a mouse button")
    label.pack(side = "bottom")
    callback.label = label
    
    canvas = Canvas(frame, cursor = "dot")
    canvas.pack(side = "left", fill = "both", expand = 1)

    canvas.bind("<Button-1>", callback)
    canvas.bind("<Button-2>", callback)
    canvas.bind("<Button-3>", callback)


main()





