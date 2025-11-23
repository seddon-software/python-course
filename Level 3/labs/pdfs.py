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

# add your code here

