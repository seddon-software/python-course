import calendar, os
import os
import openpyxl

# define year
YEAR = 2024

def coroutine(worksheet, range):
    ''' 
    This coroutine reads in a value (through yield)
    and writes it to the next cell in a given cell range
    '''
    rows = openpyxl.utils.cell.rows_from_range(range)
    for row in rows:
        # get id of each cell ("A1", "A2" etc)
        for id in row:
            value, bold = yield
            worksheet[id] = value 
            worksheet[id].font = openpyxl.styles.Font(bold=bold)    
    return

def setSizesOfCells(ws):
    for col in range(1, 50):
        letter = openpyxl.cell.cell.Cell(ws, row=3, column=col).column_letter
        ws.column_dimensions[letter].width = 12  # approx 12*7 pixels
    for col in range(2, 9):
        letter = openpyxl.cell.cell.Cell(ws, row=3, column=col).column_letter
        ws.column_dimensions[letter].width = 4  # approx 4*7 pixels
    for row in range(1, 1000):
        ws.row_dimensions[row].height = 21.0*0.7
        
def setDays(year, iterator, comments=False):
    ''' 
    this routine sets all the days in the year using Calendar.yeardayscalendar()
    when comments=True the calendar is reproduced to one side with all the days blank 
    so I can add comments
    '''

    def sendSpaces(n):
        for spaces in range(n): iterator.send(("", False))

    try:
        c = calendar.Calendar()
 
        # write out each month
        yeardays = c.yeardayscalendar(year, 12)      # 12 months per row
        for months in yeardays:
            for i, month in enumerate(months):
                for week in month:
                    if 1 in week: 
                        # spacing before and after month name
                        sendSpaces(10)
                        iterator.send((f"{calendar.month_name[i+1]}", True))
                        sendSpaces(3)
                        # add days of the week
                        iterator.send(("M", True))
                        iterator.send(("Tu", True))
                        iterator.send(("W", True))
                        iterator.send(("Th", True))
                        iterator.send(("F", True))
                        iterator.send(("Sa", True))
                        iterator.send(("Su", True))
                    for day in week:
                        if day == 0: day = ""       # blanks for days not in month
                        if comments: day = ""
                        iterator.send((f"{day}", False))
    except:
        pass


def main():
    # define workbook
    fileName = 'data/calendar.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"{YEAR}"


    # create iterator for range of cells
    iterator = coroutine(ws, "B1:H120")      # enough cells for a complete year
    iterator.send(None)     # to start coroutine
    setDays(YEAR, iterator)
    iterator = coroutine(ws, "J1:P120")      # enough cells for the comments
    iterator.send(None)     # to start coroutine
    setDays(YEAR, iterator, comments=True)
    setSizesOfCells(ws)

    # save the workbook
    wb.save(fileName)
    cmd = f"libreoffice {fileName}"
    os.system(cmd)

main()
