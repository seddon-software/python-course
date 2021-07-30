import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".rotate.jpg"
try:
    img = Image.open(infile)    
    img = img.rotate(45)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
