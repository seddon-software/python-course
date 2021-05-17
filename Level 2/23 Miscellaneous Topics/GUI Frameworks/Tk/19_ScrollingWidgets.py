############################################################
#
#	Scrolling Widgets
#
############################################################

from tkinter import *
    
def main():
    root = Tk()
    root.title("Scrolling Widgets")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text = Text(frame, wrap=WORD, width = 40, yscrollcommand=scrollbar.set)
    text.pack(expand = 2, fill = "both")
    scrollbar.config(command=text.yview)

    for word in ("FirstName", "LastName", "Address1", "Address2", "Address3", "Address4",
                 "Email", "Telephone", "Department", "Subject1", "Subject2", "Subject3", "Subject4"):
        label = Label(text, text = word, relief = "groove", width = 20)
        entry = Entry(text, width = 20)
        entry.insert(0, "default value")
        text.window_create("end", window = label)
        text.window_create("end", window = entry)
        text.insert('end', "\n")

    
main()




