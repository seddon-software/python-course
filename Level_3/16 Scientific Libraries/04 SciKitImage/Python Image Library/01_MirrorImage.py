import os, sys
from PIL import Image


os.chdir("images")
infile = "plastic_container.JPG"
#infile = "car.jpeg"
outfile = os.path.splitext(infile)[0] + ".flipped.jpg"
try:
    img = Image.open(infile)
    print(img.size)
    img = img.resize((800, 600))

    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
except IOError as e:
    print(e)
    