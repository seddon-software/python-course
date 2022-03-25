'''
Black and White
===============

To convert a color image to balack and white use:
            img = img.convert("1")

Greyscale images are monocrome, with only black (0) and white (255) pixel values.


The L denotes a specific algorithm used to perform the conversion.  For more details go to:
    https://pillow.readthedocs.io/en/latest/reference/Image.html?highlight=convert#PIL.Image.Image.convert
'''

import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".blackwhite.jpg"
try:
    img = Image.open(infile)
    img = img.convert("1")
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
