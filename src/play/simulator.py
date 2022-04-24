import sys
import curses

stdscr = curses.initscr()

# STACK_COL = 50
VALUE_COL = 53
VARIABLE_COL = 62
DEBUG = True if len(sys.argv) == 1 else False 

def debug(text):
    output(2, 60, str(text), curses.color_pair(1))
    refresh()

def start():
#    curses.cbreak()
    curses.nocbreak()
    curses.curs_set(0)
#    setup_colors()

def finish():
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def refresh():
    stdscr.refresh()

def output(row, col, text, color=None):
    try:
        if color == None: color = curses.color_pair(1)
        stdscr.addstr(row, col, text, color)
        row += 1
    except Exception as e:
        print(e)
    return row

def wait():
    if not DEBUG: 
        stdscr.getch()

class Code:
    '''
    self.index = index of code line
    self.row = screen row of start line of code 
    '''
    def __init__(self, row, col, code):
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
        line = self.code[self.index]
        output(new_row, self.col_const, line, Thread.current_thread.get_color())
        self.previous_row = new_row
        self.previous_line = self.code[self.index]
        refresh()
        wait()

class Color:
    def __init__(self):
        try:
            curses.start_color()
            if(not curses.has_colors()): raise Exception()
        except Exception as e:
            print("no colors")
            sys.exit(1)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        stdscr.bkgd(0, curses.color_pair(1))

class Thread:
    current_thread = None

    def __init__(self, color1, color2):
        self.color1 = color1
        self.color2 = color2
        self.current_color = color1

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
        stack.add(self)
    
    def set(self, rhs):
        if isinstance(rhs, int):
            self.value = rhs
        else:
            self.value = rhs.value
        self.print()

    def __iadd__(self, rhs):
        self.value += rhs.value
        self.print()
        return self

    def getRowOffset(self):
        return self.stack.rowOffset(self)

    def print(self):
        stack = self.stack
        width = stack.width
        row = stack.row + self.getRowOffset()
        col = stack.col + width//2 - 2
        blanks = " "*7
        output(row, col, blanks)
        output(row, col, str(self.value), Thread.current_thread.get_color())

    def show(self):
        stack = self.stack
        width = stack.width
        row = stack.row + self.getRowOffset()
        col = stack.col + width + 1
        output(row, col, self.name)

