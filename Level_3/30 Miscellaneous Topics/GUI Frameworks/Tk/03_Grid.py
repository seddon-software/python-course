############################################################
#
#	Grid
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Grid")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.grid()
    draw(root, mainframe)
    root.mainloop()

def draw(root, frame):
    b1 = Button(frame, text = "1")
    b2 = Button(frame, text = "2")
    b3 = Button(frame, text = "3")
    b4 = Button(frame, text = "4")
    b5 = Button(frame, text = "5")
    b6 = Button(frame, text = "6")
    b7 = Button(frame, text = "7")
    b8 = Button(frame, text = "8")
    
    # form a 2 row by 4 col grid
    # where row 0 sticks to N
    # and row 1 sticks to all four sides
    # when resizing your window
    
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=1, column=0)
    b6.grid(row=1, column=1)
    b7.grid(row=1, column=2)
    b8.grid(row=1, column=3)
    
    # weights of each row and column must be set if you
    # want your widgets to resize with the window
     
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 5)
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 5)


main()





