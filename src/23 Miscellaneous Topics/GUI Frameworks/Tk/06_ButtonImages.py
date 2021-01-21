############################################################
#
#	Button Images
#
############################################################


# note that Tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from "http://www.pythonware.com/products/pil/index.htm"
 
from tkinter import *

def calculate():
    print("Button clicked")


def main():
    root = Tk()
    root.title("Button Images")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    imageRadio = PhotoImage(file="GIFs/radio.gif")
    
    Button(frame,
           image=imageRadio, 
           text="Image Button", 
           background="blue", 
           activebackground="red", 
           command=calculate).pack(side=LEFT, padx=2, pady=2)

    # hold on a reference to image to stop GC
    frame.ref = imageRadio

main()

