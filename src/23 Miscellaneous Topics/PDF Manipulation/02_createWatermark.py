from reportlab.pdfgen import canvas

point = 10
inch = 72

TEXT = "watermark"

def make_pdf_file(output_filename):
    title = output_filename
    h = 8.5 * inch
    v = 11 * inch
    grey = 0.9
    c = canvas.Canvas(output_filename, pagesize=(h, v))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(grey, grey, grey)
    c.setFont("Helvetica", 12 * point) 
    c.rotate(45)
    c.translate(h/2, 0)

    c.drawString(-h/8, 0, TEXT )
    c.showPage()
    c.save()
    
filename = "pdfs/watermark.pdf"
make_pdf_file(filename)
print(("Wrote", filename))