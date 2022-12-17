############################################################
#
#    Sudoku
#
############################################################



from tkinter import *
import tkinter as tk
from enum import Enum
import copy
import re
import functools as ft
import scrape_sudoku

class History:
    def __init__(self):
        self.moves = []
        self.index = -1
        
    def addMove(self):
        move = []
        for cell in cells:
            move.append(copy.copy(cell.data))
        self.moves.append(move)
        self.index = len(self.moves) - 1
        
    def getPrevious(self, n=1):
        if self.index < n: raise ValueError()
        self.index -= n      
        return self.moves[self.index]
    
    def getNext(self, n=1):
        if self.index > len(self.moves) - (n+1): raise ValueError()
        self.index += n      
        return self.moves[self.index]
    
    def store(self, move):
        self.moves.append(move)
        for data, cell in zip(move, cells):
            cell.data = copy.copy(data)

        
class Cell:
    def __init__(self, frame):
        self.text = Text(frame, relief=SUNKEN, height=3, width=3, borderwidth=2, spacing1=3, spacing3=3)
        self.text.parent = self         # let text know its parent
        self.data = list(range(0,10))   # element 0 only used in toggle
        self.display()
        self.setting = False

    def setColor(self, color):
        self.text.configure(background=color)    
    
    def toggle(self, n):
        if self.setting:
            self.setSolution(n)
            self.setting = False
        else:
            self.data[n] = n if self.data[n] == 0 else 0

    def unset(self, n):
        self.data[n] = 0
        
    def getText(self):
        return self.text

    def isSolved(self):
        candidates = set(self.data)
        candidates.remove(0)
        return (len(candidates) == 1)

    def setSolution(self, n):
        self.data = [0]*10
        self.data[n] = n
           
    def getSolution(self):
        candidates = set(self.data)
        candidates.remove(0)
        assert len(candidates) == 1
        return candidates.pop()
            
    def display(self):
        if self.isSolved():
            s = f" {self.getSolution()} "
            textSize = 36
            self.text.config(height=1, width=1, spacing1=12)
        else:
            chars1 = [f" {c} " if c != 0 else '   ' for c in self.data[1:4]]
            chars2 = [f" {c} " if c != 0 else '   ' for c in self.data[4:7]]
            chars3 = [f" {c} " if c != 0 else '   ' for c in self.data[7:10]]
            s1 = "".join(chars1)
            s2 = "".join(chars2)
            s3 = "".join(chars3)            
            s = f"{s1}\n{s2}\n{s3}\n"
            textSize = 14
            self.text.config(height=3, width=3, spacing1=3, spacing3=3)
#            self.text.config(bg="red")
        self.text.delete(1.0, END)
        self.text.insert(1.0, s)
        self.text.config(font=("Courier", textSize))
        self.text.tag_configure("center", justify='center')
        self.text.tag_add("center", 1.0, "end")        

class Block:    
    def __init__(self, parent, id):
        self.frame = Frame(parent, relief=FLAT, background = "black", bd=2)
        self.id = id
        
    def getFrame(self):
        return self.frame
    

def addButtons(frame):
    frame.grid_columnconfigure(3, weight=30, pad=20)
    frame.grid_columnconfigure(4, weight=30, pad=20)
    Button(frame, text="<",    fg="blue", highlightbackground="green", height=2, 
           command=undoHistory).grid(column=3, row=0, sticky=E)
#     Button(frame, text=">",    fg="blue", highlightbackground="green", height=2, 
#            command=redoHistory).grid(column=3, row=1, sticky=E)
           
    Button(frame, text="<<",    fg="blue", highlightbackground="green", height=2, 
           command=ft.partial(undoHistory,3)).grid(column=4, row=0, sticky=E)
#     Button(frame, text=">>",    fg="blue", highlightbackground="green", height=2, 
#            command=ft.partial(redoHistory,3)).grid(column=4, row=1, sticky=E)

def repaint():
    for cell in cells:
        cell.display()

def undoHistory(n=1): 
    global history
    try:
        move = history.getPrevious(n)
        history.store(move)
        repaint()
    except ValueError as e:
        pass        # no undos left

def redoHistory(n=1): 
    global history
    try:
        move = history.getNext(n)
        history.store(move)
        repaint()
    except ValueError as e:
        pass        # no undos left

def createFrame(window, r, c, colour, text=""):
    # frame = Frame(window, relief=FLAT, background = colour, bd=1)
    block = Block(window, 3*r+c)
    frame = block.getFrame()
    frame.grid(row=r, column=c, sticky=W+E+N+S)
    
    frame.grid_rowconfigure(0, weight=30)
    frame.grid_rowconfigure(1, weight=30)
    frame.grid_rowconfigure(2, weight=30)
    frame.grid_columnconfigure(0, weight=30)
    frame.grid_columnconfigure(1, weight=30)
    frame.grid_columnconfigure(2, weight=30)

    for row in range(3):
        for col in range(3):
            cell = Cell(frame)
            textBox = cell.getText()
            cells.append(cell)
            textBox.grid(row=row, column=col, sticky=E+W+N+S)
            cell.square = r * 3 + c
            cell.row = r * 3 + row
            cell.column = c * 3 + col
            textBox.bind("<KeyPress>", onKeyPress)
 
def drawGrid(frame):
    for row in range(3):
        for col in range(3):
            createFrame(window=frame, r=row, c=col, colour='blue')
def initialize(initialCells):
    def g():
    # 0 1 2 3 4 5 6 7 8 9 .. 81 ->  
    #                     0  1  2  9 10 11 18 19 20
    #                     3  4  5 12 13 14 21 22 23
    #                     6  7  8 15 16 17 24 25 26
    #                    27 28 29 36 37 38 45 46 47
    #                    30 31 32 39 40 41 48 49 50
    #                    33 34 35 42 43 44 51 52 53
    #                    54 55 56 63 64 65 72 73 74
    #                    57 58 59 66 67 68 75 76 77
    #                    60 61 62 69 70 71 78 79 80
        endRow = [3,6,9,30,33,36,57,60,63,12,15,18,39,42,45,66,69,72]
        endCol = [21,24,48,51,75,78]
        n = 0
        while n < 81:
            if n in endCol: n -= 18
            elif n in endRow: n += 6
            else: pass
            yield n
            n += 1
        return
    
    chars = [c for c in initialCells]
    # chars needs to be transformed using generator g
    values = ""
    for n in g():
        values += chars[n]
    
    for cell, c in zip(cells, values):
        if c != "-":
            cell.setSolution(int(c))
            
                    
def main():
    root = tk.Tk()
    root.title("Sudoku")
    mainframe = tk.Frame(master=root)
    mainframe.pack(padx=100, pady=50)
    mainframe.grid_columnconfigure(0, weight=0, minsize=300)
    mainframe.grid_columnconfigure(1, weight=0, minsize=300)
    mainframe.grid_columnconfigure(2, weight=0, minsize=300)
    drawGrid(mainframe)
    addButtons(mainframe)
    initialCells = '''
                   5--8-----
                   -18-----3
                   7--1-6---
                   92------6
                   --7-5----
                   6859--4--
                   --2-9-8-7
                   ---------
                   --4----32
                   ''' 
    # initialCells = scrape_sudoku.getPuzzle()
    initialCells = re.sub(r'\s', '', initialCells)  # remove white space
    initialize(initialCells)
    removeCandidates()
    setColors()
    refresh()
    root.mainloop()

def onKeyPress(event):
    '''
    Press key in range 1-9 to toggle candidate
    Press = followed by key in range 1-9 to set value
    '''
    def getDigit():
        try:
            n = int(event.char) - int('0')
        except:
            n = 0
        return n
    textBox = event.widget
    cell = textBox.parent

    n = getDigit()
    if event.char == "=":
        cell.setting = True
    else:
        cell.toggle(n)
        
    # refresh grid if 1 .. 9 entered
    if n in list(range(1,10)): refresh()
    
    return "break"

def refresh():
    global history
    
    # the first pass may solve more cells
    # and hence this needs to be called multiple times
    for _ in range(6):
        removeCandidates()
        
    for cell in cells:
        cell.display()
    history.addMove()
    print(history.index)

################################### TODO ###############################
def isRowPair(cell):
    for cellA in cells:
        if not cellA.isSolved():
            pass
    
################################### TODO ###############################
def isColumnPair(cell):
    for cellA in cells:
        if not cellA.isSolved():
            pass
    
def removeCandidates():
    def isSameRow(cellA, cellB): return cellA.row == cellB.row
    def isSameColumn(cellA, cellB): return cellA.column == cellB.column
    def isSameSquare(cellA, cellB): return cellA.square == cellB.square

    for cellA in cells:
        if cellA.isSolved():
            solution = cellA.getSolution()
            for cellB in cells:
                if cellA is cellB: continue
                if isSameRow(cellA, cellB): cellB.unset(solution)
                if isSameColumn(cellA, cellB): cellB.unset(solution)
                if isSameSquare(cellA, cellB): cellB.unset(solution)

def setColors():
    for cell in cells:
        n = cell.square % 2
        if n == 0: cell.setColor("#ffffee")
        if n == 1: cell.setColor("#ffeeff")

cells = []
history = History()     # singleton object
main()
