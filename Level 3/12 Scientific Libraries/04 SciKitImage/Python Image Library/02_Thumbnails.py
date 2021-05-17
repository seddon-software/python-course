import os, sys
from PIL import Image

size = 128, 128

os.chdir("images")
infile = "DSCF0437.JPG"

outfile = os.path.splitext(infile)[0] + ".thumbnail-128.jpg"
try:
    img = Image.open(infile)
    img.thumbnail(size)
    img.show()
    img.save(outfile, "JPEG")
except IOError:
    print(e)
