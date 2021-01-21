############################################################
#
#	Disabling Buttons
#
############################################################

# demonstrate changing a button's colour when active and
# toggling the button between enabled and disabled


def callback():
    # toggle the state of the exit button
    buttonExit = callback.buttonExit
    
    if(buttonExit.cget("state") == "disabled"):
        title = "Disable Exit"
        buttonExit.configure(state = "normal")
    else:
        title = "Enable Exit"
        buttonExit.configure(state = "disabled")


from tkinter import *

def main():
    root = Tk()
    root.title("Disabling Buttons")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    buttonExit = Button(frame, 
                        text = "Exit",
                        activebackground = "red", 
                        command = lambda : exit())
    title = StringVar()
    title.set("Disable Exit")
    buttonToggle = Button(frame, 
                          textvariable = title, 
                          command = callback)
    buttonToggle.pack()
    buttonExit.pack()
    callback.buttonExit = buttonExit


main()




