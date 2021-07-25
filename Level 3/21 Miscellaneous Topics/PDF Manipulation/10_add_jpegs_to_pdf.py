import os
from PIL import Image
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

outfile = 'out/deeds.pdf'

def addJpg(fileName, canvas):
    image = Image.open(fileName)
    image = image.transpose(Image.ROTATE_270)
    readerImage = ImageReader(image)
    canvas.drawImage(readerImage, x=0, y=0, width=A4[0], height=A4[1], preserveAspectRatio=True)
    canvas.showPage()

def main():
    c = canvas.Canvas(outfile, pagesize=portrait(A4))    
    
    os.chdir("images")
    fileNames = []
    for fileName in os.listdir("."):
        if fileName.endswith(".jpg"):
            fileNames.append(fileName)
    
    fileNames.sort()
    
    for fileName in fileNames:
        print(fileName)
        addJpg(fileName, c)
    
    os.chdir("..")
    print(f"saving {outfile}")    
    c.save()

main()
