############################################################
#
#	Reading A File
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Reading A File")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()


def readInputFile(text):
    try:
        f = open("files/myfile.txt", "r")
        for line in f:
            text.insert(END, line)
    
    except IOError as e:
        print(e)
    else:
        f.close()

def draw(frame):
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set)
    text.pack()    
    scrollbar.config(command=text.yview)

    text.configure(background = "yellow", 
                   foreground = "blue", 
                   height = 10,
                   font = "Arial 16", 
                   wrap = "none")
    
    readInputFile(text)


main()


