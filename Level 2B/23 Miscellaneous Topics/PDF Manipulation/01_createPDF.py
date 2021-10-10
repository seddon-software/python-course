from reportlab.pdfgen import canvas

point = 1
inch = 72
filename = "pdfs/simple.pdf"

c = canvas.Canvas(filename, pagesize=(8.5 * inch, 11 * inch))
c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)
c.setFont("Helvetica", 12 * point) 


def addPage(lines):
    v = 10 * inch
    for line in lines:
        c.drawString( 1 * inch, v, line)
        v -= 14 * point
    c.showPage()

addPage(["Page 1", "Goodbye", "Universe"])
addPage(["Page 2", "More lines", "of text"])
addPage(["Page 3", "This is famous in the UK"])
addPage(["Page 4"])
addPage(["Page 5 - line 1", "line 2", "line 3", "line 4", "line 5", "line 6", "line 7"])

c.save()
print("{0} created".format(filename))
    
