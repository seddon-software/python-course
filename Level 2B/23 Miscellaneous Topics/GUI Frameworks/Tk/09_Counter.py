############################################################
#
#	Counter
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Counter")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def EverySecond():
    n = EverySecond.count.get() + 1
    EverySecond.count.set(n)
    EverySecond.frame.after(1000, EverySecond)

def draw(frame):
    count = IntVar()
    label = Label(frame, width=10, textvariable=count, font = "Arial 40")
    label.pack()
    EverySecond.count = count
    EverySecond.frame = frame
    frame.after(1000, EverySecond)


main()



