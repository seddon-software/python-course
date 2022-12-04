'''
Contours
========

The Contours filter applies an edge detector algorithm to pick out objects in an image.  
    img = img.filter(ImageFilter.CONTOUR)

In this image the trees provide very detailed edges.  Probably best to use with a simpler image.
'''

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
