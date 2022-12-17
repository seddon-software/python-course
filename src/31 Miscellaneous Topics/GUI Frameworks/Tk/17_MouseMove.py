############################################################
#
#	Mouse Move
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Mouse Move")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def TrackMouse(event):
    x, y = event.x, event.y 
    coords = (x, y, x + 20, y + 20)
    options = {'width':1.0, 'fill':"red", 'outline':"blue"}
    TrackMouse.canvas.create_oval(coords, **options);

def TrackMouseMiddleButton(event):
    x, y = event.x, event.y 
    coords = (x, y, x + 10, y + 10)
    options = {'width':2.0, 'fill':"green", 'outline':"white"}
    TrackMouseMiddleButton.canvas.create_oval(coords, **options);


def draw(frame):
    canvas = Canvas(frame, cursor = "pencil")
    canvas.pack(side = "left", fill = "both", expand = 1)
    TrackMouse.canvas = canvas
    TrackMouseMiddleButton.canvas = canvas
    canvas.bind("<Motion>", TrackMouse);
    canvas.bind("<B2-Motion>", TrackMouseMiddleButton);


main()





