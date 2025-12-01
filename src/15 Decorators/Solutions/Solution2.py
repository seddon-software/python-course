'''
'''

import sys, io, os
from openpyxl import Workbook

def spreadsheet(fn):
    def inner(fileName, column):
        # switch stdout
        output = io.StringIO()
        sys.stdout = output

        # open workbook
        wb = Workbook()
        ws = wb.active
        ws.title = f"{fileName}"

        # call decorated function
        fn()

        # extract output and write to spreadshhet in seleted column
        captured_output = output.getvalue().split("\n")
        for n, text in enumerate(captured_output):
            ws[f'{column}{n+1}'] = text
        wb.save(fileName)

        # look at spreadsheet
        cmd = f"libreoffice {fileName}"
        os.system(cmd)

        # reset stdout
        sys.stdout = sys.__stdout__
    return inner


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@spreadsheet
def daysOfTheWeek():
    for day in days:
        print(day)

@spreadsheet
def monthsOfTheYear():
    for month in months:
        print(month)


daysOfTheWeek("f1.xlsx", "B")
monthsOfTheYear("f2.xlsx", "D")

