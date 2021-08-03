############################################################
#
#	Button Styles
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Button Styles")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()


def draw(frame):
    b1 = Button(frame, text = "flat button")
    b2 = Button(frame, text = "groove button")
    b3 = Button(frame, text = "raised button")
    b4 = Button(frame, text = "ridge button")
    b5 = Button(frame, text = "sunken button")
    b6 = Button(frame, text = "solid button")

    b1.configure(relief = "flat",   background = "#ff0000")
    b2.configure(relief = "groove", background = "#df2020")
    b3.configure(relief = "raised", background = "#bf4040")
    b4.configure(relief = "ridge",  background = "#9f6060")
    b5.configure(relief = "sunken", background = "#7f8080")
    b6.configure(relief = "solid",  background = "#5fa0a0")
    
    b1.pack(pady=10)
    b2.pack(pady=100)
    b3.pack(pady=10)
    b4.pack(pady=10)
    b5.pack(pady=10)
    b6.pack(pady=10)

main()
 