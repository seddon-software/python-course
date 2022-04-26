from inspect import stack
import os, sys
from sqlite3 import Row
import curses
import __main__

stdscr = curses.initscr()

def debug(text):
    output(2, 60, str(text), curses.color_pair(1))
    refresh()

def start():
#    curses.cbreak()
    curses.curs_set(0)

def finish():
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit()

def wait():    
    if not os.environ.get('TERM_PROGRAM') == "vscode": 
        stdscr.keypad(True)
        ch = stdscr.getch()
        if ch == -1: finish()    # terminate on Ctl-C
        stdscr.keypad(False)

def refresh():
    stdscr.refresh()

def output(row, col, text, color=None):
    try:
        if color == None: color = curses.color_pair(1)
        stdscr.addstr(row, col, text, color)
        row += 1
    except Exception as e:
        if not os.environ.get('TERM_PROGRAM') == "vscode": 
            print(e)
    return row

class Message:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __call__(self, text="", max=50):
        row = self.row
        col = self.col
        blanks = " "*max
        output(row, col, blanks, curses.color_pair(6))
        output(row, col, text, curses.color_pair(6))
        refresh()
        wait()
        output(row, col, blanks, curses.color_pair(6))
        refresh()

class Code:
    '''
    self.index = index of code line
    self.row = screen row of start line of code 
    '''
    def __init__(self, row, col):
        code = __main__.__doc__
        self.row_const = row
        self.col_const = col
        self.code = code.split("\n")
        self.index = 0
        self.previous_row = None
        self.show()

    def show(self):
        row = self.row_const
        for line in self.code:
            row = output(row, self.col_const, line, curses.color_pair(1))
        refresh()

    def step(self, rows=1):
        col = self.col_const
        if(self.previous_row): output(self.previous_row, col, self.previous_line, curses.color_pair(1))
        self.index += rows
        new_row = self.index + self.row_const
        try:
            line = self.code[self.index]
            output(new_row, self.col_const, line, Thread.current_thread.get_color())
            self.previous_row = new_row
            self.previous_line = self.code[self.index]
            refresh()
            wait()
        except:
            pass    # no more code

class Color:
    def __init__(self):
        try:
            curses.start_color()
            if(not curses.has_colors()): raise Exception()
#            print(f"Can we use extended colors? {curses.has_extended_color_support()}")
        except Exception as e:
            print("no colors")
            sys.exit(1)
        curses.init_color(31, 0, 1000, 0)
        curses.init_color(32, 0,  700, 300)
        curses.init_color(41, 1000, 0, 0)
        curses.init_color(42, 700, 300, 0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, 31, curses.COLOR_BLACK)
        curses.init_pair(3, 32, curses.COLOR_BLACK)
        curses.init_pair(4, 41, curses.COLOR_BLACK)
        curses.init_pair(5, 42, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_YELLOW)
        stdscr.bkgd(0, curses.color_pair(1))

class Thread:
    current_thread = None

    def __init__(self, color1, color2):
        self.color1 = color1
        self.color2 = color2
        self.current_color = color1
        self.activate()

    def activate(self):
        Thread.current_thread = self

    def swap_colors(self):
        if self.current_color == self.color1:
            self.current_color = self.color2
        else:
            self.current_color = self.color1

    def get_color(self):
        return curses.color_pair(self.current_color)

class Stack:
    def __init__(self, row, col, boxes):
        self.row = row
        self.col = col
        self.boxes = boxes
        self.variables = []
        self.draw_stack()
        self.width = 11

    def draw_stack(self):
        boxes = self.boxes
        row = self.row
        col = self.col 
        row = output(row, col, "┌─────────┐");
        for i in range(boxes-1):
            row = output(row, col, "│         │");
            row = output(row, col, "├─────────┤");
        row = output(row, col, "│         │");
        row = output(row, col, "└─────────┘");

    def add(self, variable):
        self.variables.append(variable)
    
    def rowOffset(self, variable):
        index = self.variables.index(variable)
        return 2*index + 1

class Variable:
    def __init__(self, name, stack, value):
        self.name = name
        self.stack = stack
        self.value = value
        self.hasArrow = False
        stack.add(self)
    
    def set(self, rhs):
        '''sets variable and updates screen'''
        if isinstance(rhs, Variable):
            self.value = rhs.value
        else:
            self.value = rhs
        self.print()

    def getRowOffset(self):
        return self.stack.rowOffset(self)

    def print(self, hide=False):
        '''prints the value on screen'''
        stack = self.stack
        width = stack.width
        row = stack.row + self.getRowOffset()
        col = stack.col + width//2 - 2
        blanks = " "*7
        output(row, col, blanks)
        if not hide: output(row, col, str(self.value), Thread.current_thread.get_color())

    def show(self):
        '''displays variable on screen'''
        stack = self.stack
        width = stack.width
        row = stack.row + self.getRowOffset()
        col = stack.col + width + 1
        output(row, col, self.name)

    def hide(self):
        stack = self.stack
        width = stack.width
        row = stack.row + self.getRowOffset()
        col = stack.col + width + 1
        blanks = " "*len(self.name)
        output(row, col, blanks)
        self.print(hide=True)
        if self.hasArrow:
            self.arrow(self.to, hide=True)

    def arrow(self, to, hide=False):
        if (self.stack.row + self.getRowOffset()) == (to.stack.row + to.getRowOffset()):
            self.arrowStraight(to, hide)
        else:
            self.arrowDogLeg(to, hide)
    
    def arrowStraight(self, to, hide=False):
        self.hasArrow = True
        self.to = to
        row = to.stack.row + to.getRowOffset()
        col = self.stack.col + self.stack.width + len(self.name) + 1
        count = to.stack.col - self.stack.col - self.stack.width - len(self.name) - 2
        if hide:
            text = " "*(count+1)
        else:
            text = "─"*count + "➤"
        output(row, col, text, curses.color_pair(1))

    def arrowDogLeg(self, to, hide=False):
        self.hasArrow = True
        self.to = to
        to_row = to.stack.row + to.getRowOffset()
        self_row = self.stack.row + self.getRowOffset()
            
        col = self.stack.col + self.stack.width + len(self.name) + 1
        count = to.stack.col - self.stack.col - self.stack.width - len(self.name)

        leftCount = count//2
        rightCount = count-leftCount

        if not hide:
            leftText = "─"*(leftCount-1) + "┐"
            rightText = "└" + "─"*(rightCount-2) + "➤"
            output(self_row, col, leftText, curses.color_pair(1))
            while self_row != to_row:
                output(self_row+1, col+leftCount-1, "│", curses.color_pair(1))
                self_row += 1
            output(to_row, col+leftCount-1, rightText, curses.color_pair(1))
        else:
            leftText = " "*(leftCount-1) + " "
            rightText = " " + " "*(rightCount-2) + " "
            output(self_row, col, leftText, curses.color_pair(1))
            refresh()
            while self_row != to_row:
                output(self_row+1, col+leftCount-1, " ", curses.color_pair(1))
                refresh()
                self_row += 1
            output(to_row, col+leftCount-1, rightText, curses.color_pair(1))
            refresh()

