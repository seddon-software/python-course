from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import math

def main():
    inFile = "pdfs/python_tutorial.pdf"
    outFile = "pdfs/python_tutorial-with-pages-merged-in-pairs.pdf"
    input = PdfFileReader(open(inFile, "rb"))
    output = PdfFileWriter()
    
    inch = 72
    h = horizontal = 8.5 * inch
    v = vertical = 11 * inch
    for page in range (0, input.getNumPages(), 2):
        print(str(page))
        lhs = input.getPage(page)
        lhs.scaleTo(h/2, v)
        try: 
            print(str(page+1))
            rhs = input.getPage(page+1)
            rhs.scaleTo(h/2, v)
            lhs.mergeTranslatedPage(rhs, v/2, 0, True)
        except: 
            pass   # if the PDF has an odd number of page, you can't merge on the last page
        output.addPage(lhs)
 
    print("writing ")
    outputStream = open(outFile, "wb")
    output.write(outputStream)
    print("done.")

if __name__ == "__main__":
    main()
