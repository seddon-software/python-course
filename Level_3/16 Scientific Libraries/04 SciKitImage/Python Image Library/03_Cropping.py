import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"

outfile = os.path.splitext(infile)[0] + ".cropped.jpg"
try:
    img = Image.open(infile)
    box = (450, 300, 1500, 1500)
    img = img.crop(box)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
