############################################################
#
#	Bitmap Images
#
############################################################


# note that Tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from "http://www.pythonware.com/products/pil/index.htm"
 
from tkinter import *
from PIL import Image, ImageTk

def calculate():
    print("Button clicked")


def main():
    root = Tk()
    root.title("Playing Cards")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def EverySecond():
    # get parameters
    card, label, frame = EverySecond.params 

    # do the work
    card = card % 52
    card = card + 1 
    filename = "BMPs/BMP" + str(card) + ".bmp"
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label.image = photo # keep a reference!
    label.configure(image = photo)
    
    # save parameters
    EverySecond.params = [ card, label, frame ]
    frame.after(1000, EverySecond)

def draw(frame):
    card = 0
    image = Image.open("BMPs/Blank.bmp")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.pack()
    EverySecond.params = [ card, label, frame ]
    frame.after(1000, EverySecond)

main()

