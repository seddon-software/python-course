'''
Mirror Image
============

The PIL (Pillow) module has simple methods for manipulating images.  Let's start with a mirror image:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)

Information on PIL (Pillow) can be found at:
                https://github.com/python-pillow/Pillow/blob/main/README.md
'''

import os, sys
from PIL import Image
import PIL

print(PIL.__doc__)
os.chdir("images")
infile = "plastic_container.JPG"
outfile = os.path.splitext(infile)[0] + ".flipped.jpg"
try:
    img = Image.open(infile)
    print(img.size)
    img = img.resize((800, 600))

    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
except IOError as e:
    print(e)
    