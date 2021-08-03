import os, sys
from PIL import Image, ImageFilter


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".contour.jpg"
try:
    img = Image.open(infile)
    img = img.filter(ImageFilter.CONTOUR)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
