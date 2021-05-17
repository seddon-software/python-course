############################################################
#
#	Checkbuttons
#
############################################################

# set up 3 checkbuttons and display their status in a
# button widget (its display name);

  
from tkinter import *

def main():
    root = Tk()
    root.title("Check Buttons")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()



def callback():
    v1 = callback.value1.get()
    v2 = callback.value2.get()
    v3 = callback.value3.get()    
    message = str(v1) + str(v2) + str(v3)
    callback.status.configure(text = message)


def draw(frame):
    button = Button(frame, text="Status")
    button.pack()
    callback.status = button;

    callback.value1 = IntVar()
    callback.value2 = IntVar()
    callback.value3 = IntVar()
    callback.value1.set(0)
    callback.value2.set(1)
    callback.value3.set(0)
    
    Checkbutton(frame, text = "Checkbutton 1", 
                       variable = callback.value1,
                       command  = callback).pack()
    Checkbutton(frame, text = "Checkbutton 2", 
                       variable = callback.value2,
                       command  = callback).pack()
    Checkbutton(frame, text = "Checkbutton 3", 
                       variable = callback.value3,
                       command  = callback).pack()

# all 3 checkbuttons use the same callback method
    callback()


main()

