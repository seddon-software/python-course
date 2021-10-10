from reportlab.pdfgen import canvas
import pandas as pd
import sys
#from openpyxl.utils.cell import col
#from rope.refactor import topackage

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)        # None means all data displayed
pd.set_option('display.max_rows', None)

def readAddresses():
    column_names = ['last', 'first', 'address']
    df = pd.read_excel('addresses.xls', 'Phone Numbers', header=None, names=column_names)
#    df = df['address'].str.split(',',expand=True)
    df['address'] = df.apply(lambda row: str(row['address']).replace(", ","\n"), axis=1, raw=False)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df['label'] = df.apply(lambda row: f"{row['first']} {row['last']}\n{row['address']}\n", axis=1, raw=False)
    return df

def draw(self):
    l = Line(self.x,self.y,self.x+self.width,self.y)
    l.strokeColor = self.strokeColor
    l.strokeDashArray  = self.strokeDashArray
    l.strokeWidth = self.height
    return l

df = readAddresses()
df.drop(['last', 'first', 'address'], axis=1, inplace=True)

point = 1
inch = 72
filename = "pdfs/labels.pdf"
TOP = 11.75 * inch
LEFT_MARGIN = 0.3 * inch
TOP_MARGIN = 0.6 * inch
BOX_HEIGHT = 1.4 * inch
BOX_WIDTH = 2.6 * inch
LEFT = 3 * inch
#LINE_WIDTH = 10 * point
LINE_WIDTH = 12 * point
LABEL_ROWS = 8
LABEL_COLUMNS = 3
LABELS_PER_PAGE = LABEL_ROWS * LABEL_COLUMNS

c = canvas.Canvas(filename, pagesize=(8.3 * inch, TOP))
c.setStrokeColorRGB(0,0,0)
c.setFont("Helvetica", 12 * point) 


def addPage(p, labels):
    vertical = TOP
    size = len(labels)
    n = 0
    for n,label in enumerate(labels):
        row = n % LABEL_ROWS
        col = n // LABEL_ROWS
        vertical = TOP - TOP_MARGIN - row * BOX_HEIGHT
        horizontal = LEFT_MARGIN + col * BOX_WIDTH

        # split label into individual lines
        for line in label.split('\n'):
            vertical -= LINE_WIDTH
            c.drawString(horizontal, vertical, f"{line}")
        n += 1
    c.showPage()

for n in range(0, len(df.index)+1, LABELS_PER_PAGE):
    addPage(0, df['label'].values[n:n+LABELS_PER_PAGE])

c.save()
print("{0} created".format(filename))
    
