'''
LAB: spreadsheet, pandas and reportlab
======================================

Take a look at the file "sample.xlsx" using libreoffice; this spreadsheet has a set of names and addresses.
Your job is to use Pandas to read the spreadsheet into memory and then create a multi-page PDF file with its contents using reportlab.
The pdf should have 20 rows and 3 columns per page.  Use a 10 point 'Times-Roman' font. 
The output should look like the file: sample.pdf.

Use the drawstring method of the reportlab.pdfgen.canvas object to place each name and address on the page.
Note that drawstring uses a y coordinate that is measured from the bottom of the page.
'''

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import numpy as np
import pandas as pd


page_width, page_height = A4  # Get width and height of the page
INPUT_FILENAME = "sample.xlsx"
OUPUT_FILENAME = "sample.pdf"
TITLE = "names and addresses"
COLS = 3
ROWS = 20
FONT_SIZE = 10
LINE_HEIGHT = FONT_SIZE + 2
LEFT_MARGIN = 10
TOP_MARGIN = 20
CELL_WIDTH = int(page_width * 0.9 / COLS)

def create_pdf(file_name, i):
    c = canvas.Canvas(file_name, pagesize=A4)
    c.setTitle(TITLE)
    c.setFont('Times-Roman', FONT_SIZE)

    x = LEFT_MARGIN  # X coordinate
    y = page_height - TOP_MARGIN  # Y measured from bottom of the page
    try:
        while(True):
            row = next(i)
            if type(row) is str:
                if row == "new column":
                    x += CELL_WIDTH
                    y = page_height-TOP_MARGIN
                if row == "new page":
                    x = LEFT_MARGIN
                    y = page_height-TOP_MARGIN
                    c.showPage()
                    c.setFont('Times-Roman', FONT_SIZE)
                continue
            for text in row:
                c.drawString(x, y, text)
                y -= LINE_HEIGHT
    except StopIteration as e:
        c.save()

# generator to fetch rows
def fetch_rows(data):
    '''
    normally yield a new row, but also use the ROWS and COLS variables to signal when to create a new column or a new page
    '''
    for i,row in enumerate(data):
        if i == 0: 
            yield row
        elif i%(ROWS*COLS) == 0: 
            yield "new page"
            yield row
        elif i%ROWS == 0: 
            yield "new column"
            yield row
        else:
            yield row
    return

def get_data_from_spreadsheet():
    # Read the data
    df = pd.read_excel(INPUT_FILENAME)

    # convert to numpy
    df['blank_line'] = ""
    data = df.values
    return data

def main():
    d = get_data_from_spreadsheet()
    rows = fetch_rows(d)
    # Create the PDF
    create_pdf(OUPUT_FILENAME, rows)
    import os
    os.system(f"evince {OUPUT_FILENAME}")

if __name__ == "__main__":
    main()
