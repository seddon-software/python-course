'''
Greyscale
=========

To convert a color image to greyscale use:
            img = img.convert("L")

Greyscale images are monocrome, but include pixel value from 0 to 255.

The L denotes a specific algorithm used to perform the conversion.  For more details go to:
    https://pillow.readthedocs.io/en/latest/reference/Image.html?highlight=convert#PIL.Image.Image.convert
'''

import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".greyscale.jpg"
try:
    img = Image.open(infile)
    img = img.convert("L")
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
    