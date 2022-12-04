'''
Resize
======

You can resize an image with:
            img = img.resize((250, 250))

This shrinks the image rather than cropping it.
'''

import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".resize.jpg"
try:
    img = Image.open(infile)
    print(f"original image size: {img.size}")
    img = img.resize((250, 250))
    print(f"new image size: {img.size}")
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
