############################################################
#
#	Pack
#
############################################################

from tkinter import *

def main():
    root = Tk()
    root.title("Pack")
    root.minsize(width=300, height=300)
    mainframe = Frame(master=root)
    mainframe.pack()
    draw(mainframe)
    root.mainloop()

def draw(frame):
    b1 = Button(frame, text = "1")
    b2 = Button(frame, text = "2")
    b3 = Button(frame, text = "3")
    b4 = Button(frame, text = "4")
    b5 = Button(frame, text = "5")
    b6 = Button(frame, text = "6")
    b7 = Button(frame, text = "7")
    b8 = Button(frame, text = "8")
    b9 = Button(frame, text = "9")
    b10 = Button(frame, text = "10")
    b11 = Button(frame, text = "11")
    b12 = Button(frame, text = "12")
    
    left   = {'side':'left',   'expand':1, 'fill':'x'}
    right  = {'side':'right',  'expand':1, 'fill':'x'}
    top    = {'side':'top',    'expand':1, 'fill':'y'}
    bottom = {'side':'bottom', 'expand':1, 'fill':'y'}
    
    b1.pack(left)
    b2.pack(left)
    b3.pack(left)
    
    b4.pack(right)
    b5.pack(right)
    b6.pack(right)
    
    b7.pack(top)
    b8.pack(top)
    b9.pack(top)
    
    b10.pack(bottom)
    b11.pack(bottom)
    b12.pack(bottom)


    pass


main()
