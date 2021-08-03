############################################################
#
#	Menus
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Menus")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(root, mainframe)
    root.mainloop()


# use tkinter tracing feature : StringVar()
class Message(StringVar):
    def __init__(self, text, status):
        self.status = status
        self.text = StringVar()
        self.text.set(text)
        
    def __call__(self):
        self.status.configure(text = self.text.get());



def setUpStatusBar():
    frame = Frame(relief="ridge", borderwidth=2)
    frame.pack(side="top", anchor="n", expand=1, fill="x")
    status = Label(text="Select a menu option")
    status.pack()
    return status

def configureFileMenu(menubar, Menu, status):
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=Message("New", status))
    filemenu.add_command(label="Open", command=Message("Open", status))
    filemenu.add_command(label="Save", command=Message("Save", status))
    filemenu.add_command(label="Save as...", command=Message("Save as...", status))
    filemenu.add_command(label="Close", command=Message("Close", status))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Message("Exit", status))
    menubar.add_cascade(label="File", menu=filemenu)

def configureEditMenu(menubar, Menu, status):
    editmenu = Menu(menubar, tearoff=1)
    editmenu.add_command(label="Undo", command=Message("Undo", status))
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=Message("Cut", status))
    editmenu.add_command(label="Copy", command=Message("Copy", status))
    editmenu.add_command(label="Paste", command=Message("Paste", status))
    editmenu.add_command(label="Delete", command=Message("Delete", status))
    editmenu.add_command(label="Select All", command=Message("Select All", status))
    menubar.add_cascade(label="Edit", menu=editmenu)


def configureHelpMenu(menubar, Menu, status):
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=Message("About...", status))
    helpmenu.add_command(label="About...", command=Message("About...", status))
    menubar.add_cascade(label="Help", menu=helpmenu)

def draw(root, mw):   
    menubar = Menu(root)
    status = setUpStatusBar()
    configureFileMenu(menubar, Menu, status)
    configureEditMenu(menubar, Menu, status)
    configureHelpMenu(menubar, Menu, status)
    root.config(menu=menubar)

    
main()

  
