'''
Here we write a coroutine that reads in values and writes them to a range of cells in a spreadsheet.
Note that the coroutine is 'old' style in that it uses yield on the right hand side of
an assignment.  Such coroutine must be started by passing in None as the first 'send' parameter. 
'''

import os
import openpyxl as xl

def coroutine(worksheet, range):
    ''' 
    This coroutine reads in a value (through yield)
    and writes it to the next cell in a given cell range
    '''
    rows = xl.utils.cell.rows_from_range(range)
    for row in rows:
        # get id of each cell ("A1", "A2" etc)
        for id in row:
            value = yield
            worksheet[id] = value 
    return

# define workbook
fileName = 'data/writingToRangeOfCells.xlsx'
wb = xl.Workbook()
ws = wb.active
ws.title = "writing to range of cells"

# create iterator for range of cells
cells = "A1:K20"
iterator = coroutine(ws, cells)
cellRange = xl.worksheet.cell_range.CellRange(cells)
iterator.send(None)     # to start coroutine

# write to all cells in range
numberOfCells = cellRange.size['rows'] * cellRange.size['columns'] 
for n in range(numberOfCells):
    try:
        iterator.send(n)
    except StopIteration as e:
        pass

# save the workbook and open in libreoffice
wb.save(fileName)
os.system(f"libreoffice {fileName}")


