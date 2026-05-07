'''
Blur
====

To blur an image, either shake when you take the picture or use the blur filter:
            img = img.filter(ImageFilter.BLUR)

In this example, I've magifir=ed the blurring effect by repeatedly applying the filter.
'''

import os, sys
from PIL import Image, ImageFilter


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".blur.jpg"
try:
    img = Image.open(infile)
    # the blur effect is small, so blur multiple times
    for i in range(20):
        print(".", end=' ')
        img = img.filter(ImageFilter.BLUR)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
