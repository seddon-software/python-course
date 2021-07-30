import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".resize.jpg"
try:
    img = Image.open(infile)
    img = img.resize((250, 250))
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
