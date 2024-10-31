'''
Merge
=====

Merge doesn't merge images; it allows you to interchange the RGB channels of an image.  In the example we
change:
            r --> b
            g --> g
            b --> r

i.e. we swap red and blue channels.
'''

import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".modified.jpg"
try:
    img = Image.open(infile)
    img.load()      # shouldn't be necessary, but doesn't work without it
    r, g, b = img.split()
    img = Image.merge("RGB", (b, g, r))
    img.show();
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
