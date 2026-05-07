'''
In this exercise you create a calendar and write it to a spreadsheet.
You can achieve this in a number of ways, but we would like you to use iterators to complete this exercise.

Define the following iterators:
    monthIterator:  yields successive month names:        January, February, March ...
    cellIterator:   yields successive spreadsheet cells:  A1,B1,C1,D1,E1,F1,G1,A2,B2 ...
    
You should use the calendar module to get the month and day names and use:
        yeardays = calendar.Calendar().yeardayscalendar(year)
to help with formatting. 

Use openpyxl to create the spreadsheet.

Take a look at the file "calendar.xlsx" to see the expected output.
''' 

import calendar, os
import openpyxl
import itertools
YEAR = 2026

def monthIterator():
    pass # add your code here

def cellIterator():
    pass # add your code here

def main():
    # use this to get you started (feel free to modify)
    def openWorkbook():
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = f"{YEAR}"
        return wb,ws

    # add further code here

main()

