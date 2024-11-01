import os; os.system("clear")
'''
Display Iris Picture
====================

Iris flowers are often used as an introduction to machine learning.  This picture shows an iris as having 4 key
characteristics: 
            sepal length
            sepal width
            petal length
            petal width
'''

import PIL.Image as Image

img = Image.open("data/iris.png")
img.show()
