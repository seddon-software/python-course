############################################################
#
#	Button
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Buttons")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def calculate():
    print("Button clicked")
    
def draw(frame):
    Button(frame, 
           text="Button1", 
           activebackground="red", 
           command=calculate).grid(column=1, row=1, sticky=W)
    
    Button(frame, 
           text="Button2", 
           activebackground="yellow", 
           command=calculate).grid(column=3, row=2, sticky=E)
    
    Button(frame, 
           text="Button3", 
           activebackground="blue", 
           command=calculate).grid(column=2, row=3, sticky=W)


main()


