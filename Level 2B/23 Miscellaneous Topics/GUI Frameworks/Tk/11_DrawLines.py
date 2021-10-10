############################################################
#
#	Draw Lines
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Draw Lines")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    canvas = Canvas(frame, cursor = "crosshair")
    canvas.pack(side = "left", fill = "both", expand = 1)
    coords = ( 50,  50, 
              100, 160,
              120, 150,
              180, 350,
              100, 100)
    options = {'width':2.0, 'fill':"yellow", 'outline':"blue"}
    polygon = canvas.create_polygon(coords, **options)

main()





