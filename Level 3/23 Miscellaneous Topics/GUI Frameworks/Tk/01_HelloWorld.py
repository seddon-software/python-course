############################################################
#
#	Hello World Example
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Hello World")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    Button(frame, 
           text = "Hello World",
           command = lambda : exit()).pack()


main()



