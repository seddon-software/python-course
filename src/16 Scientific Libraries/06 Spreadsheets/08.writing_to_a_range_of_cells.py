'''
Here we write a coroutine that reads in values and writes them to a range of cells in a spreadsheet.
Note that the coroutine is 'old' style in that it uses yield on the right hand side of
an assignment.  Such coroutine must be started by passing in None as the first 'send' parameter. 
'''

import os
import openpyxl

def coroutine(worksheet, range):
    ''' 
    This coroutine reads in a value (through yield)
    and writes it to the next cell in a given cell range
    '''
    rows = openpyxl.utils.cell.rows_from_range(range)
    for row in rows:
        # get id of each cell ("A1", "A2" etc)
        for id in row:
            value = yield
            worksheet[id] = value 
    return

# define workbook
fileName = 'data/writingToRangeOfCells.xlsx'
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "writing to range of cells"

# create iterator for range of clls
iterator = coroutine(ws, "A1:K20")
iterator.send(None)     # to start coroutine

# write to all cells in range
for n in range(500):
    try:
        iterator.send(n)
    except StopIteration as e:
        pass

# save the workbook
wb.save(fileName)
cmd = f"libreoffice {fileName}"
os.system(cmd)


