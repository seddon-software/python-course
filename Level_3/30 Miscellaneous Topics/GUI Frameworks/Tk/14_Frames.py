############################################################
#
#				Frames
#
############################################################


from tkinter import *

def main():
    root = Tk()
    root.title("Frames")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def CreateFrame(window, r, c, s, colour, text):
    frame = Frame(window, background = colour)
    frame.grid(row=r, column=c, sticky=s)

    Button(frame, text = text + '1').grid(row = r + 1, column = c + 1)
    Button(frame, text = text + '2').grid(row = r + 2, column = c + 2)
    Button(frame, text = text + '3').grid(row = r + 3, column = c + 3)

def draw(frame):
    CreateFrame(window = frame, r = 0, c = 0, s = "N", colour = 'blue',   text = 'N')
    CreateFrame(window = frame, r = 0, c = 4, s = "E", colour = 'green',  text = 'E')
    CreateFrame(window = frame, r = 4, c = 0, s = "W", colour = 'yellow', text = 'W')
    CreateFrame(window = frame, r = 4, c = 4, s = "S", colour = 'white',  text = 'S')


main()





