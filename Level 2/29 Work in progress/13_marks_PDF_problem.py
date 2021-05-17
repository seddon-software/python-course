from PyPDF2 import PdfFileWriter, PdfFileReader
filename = "/Users/seddon/mark.pdf"
#from tika import parser
import pikepdf

# opens a PDF with restrictive editing enabled, but that still 
# allows printing.
with pikepdf.open(filename) as pdf:
    pdf.save("mark2.pdf")

filename = "mark2.pdf"
pdf = PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print(page.extractText())
