############################################################
#
#	Draw Rectangles
#
############################################################


from tkinter import *

def main():
    root = Tk()
    root.title("Draw Rectangles")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    canvas = Canvas(frame, cursor = "crosshair");
    canvas.pack(side = "left", fill = "both", expand = 1)
    
    x1 =  50; y1 =  50
    x2 = 300; y2 = 200
    coords = (x1, y1, x2, y2);
    
    options = {'width':5.0, 'fill':"yellow", 'outline':"blue"}
    
    rectangle = canvas.create_rectangle(coords, options)


main()







