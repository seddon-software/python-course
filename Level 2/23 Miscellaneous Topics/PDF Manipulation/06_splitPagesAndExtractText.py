import os
from PyPDF2 import PdfFileWriter, PdfFileReader

os.makedirs("out", exist_ok=True)
inputFile = "pdfs/python_tutorial.pdf"
outputFile = "out/python_tutorial"

input = PdfFileReader(open(inputFile, "rb"))

# create a set of pdfs for individual pages
for page in range(0, input.getNumPages()):
    output = PdfFileWriter()
    output.addPage(input.getPage(page))
    outFileName = "{0}.{1:02}.pdf".format(outputFile, page)
    print(outFileName)
    outputStream = open(outFileName, "wb")
    output.write(outputStream)
    outputStream.close()    

# create a set of text files using pdfs for individual pages
for page in range(0, input.getNumPages()):
    inFileName = "{0}.{1:02}.pdf".format(outputFile, page)
    outFileName = "{0}.{1:02}.txt".format(outputFile, page)
    print(outFileName)
    input = PdfFileReader(open(inFileName, "rb"))
    f = open(outFileName, "w")
    f.writelines(input.getPage(0).extractText())
    f.close()

