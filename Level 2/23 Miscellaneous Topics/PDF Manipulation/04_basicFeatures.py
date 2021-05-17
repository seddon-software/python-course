from PyPDF2 import PdfFileWriter, PdfFileReader

inputFile = "pdfs/simple.pdf"
output = PdfFileWriter()
input = PdfFileReader(open(inputFile, "rb"))
    
# add watermark to each page
for page in range(0, input.getNumPages()):
    # avoid cloning the watermark page by opening the file multiple times    
    watermarkReader = PdfFileReader(open("pdfs/watermark.pdf", "rb"))
    output.addPage(watermarkReader.getPage(0))

# add page 0, unchanged
output.getPage(0).mergePage(input.getPage(0))

# add page 1, rotated clockwise 90 degrees
output.getPage(1).mergePage(input.getPage(1).rotateClockwise(90))

# add page 2, rotated the other way:
output.getPage(2).mergePage(input.getPage(2).rotateCounterClockwise(90))

# add page 3, unchanged:
output.getPage(3).mergePage(input.getPage(3))
    
# add page 4, crop it to half size:
page4 = input.getPage(4)
page4.mediaBox.upperRight = (
    page4.mediaBox.getUpperRight_x() / 2,
    page4.mediaBox.getUpperRight_y() / 2
)
output.getPage(4).mergePage(page4)

# add remainder of pages
for page in range(5, input.getNumPages()):    
    output.getPage(page).mergePage(input.getPage(page))

# encrypt your new PDF and add a password
password = "secret"
output.encrypt(password)

# finally, write "output" to document-output.pdf
outputStream = open("pdfs/sample-with-watermark.pdf", "wb")
output.write(outputStream)
