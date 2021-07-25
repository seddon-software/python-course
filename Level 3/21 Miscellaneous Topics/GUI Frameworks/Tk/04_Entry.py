############################################################
#
#    Entry Fields
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Entry Fields")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    Label(frame, text="First").grid(row=0, column=0, sticky=W)
    Label(frame, text="Second").grid(row=1, column=0, sticky=E)
    Label(frame, text="This is the Third").grid(row=2, column=0, sticky=N)
    
    e1 = Entry(frame)
    e2 = Entry(frame)
    e3 = Entry(frame)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)


main()




