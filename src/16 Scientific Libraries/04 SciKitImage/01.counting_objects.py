import os; os.system("clear")
'''
Counting Objects
================
In this section we will be looking at using SciKitImage for processing images.  As a preamble we discuss
how an image gets converted to a Numpy array so that it can be processed.

2D Coloured images are represented by 3 dimensional arrays; the images are normally converted to Numpy arrays 
using something like:
        array = load_image("images/rice.jpg")

However in this example, we will start with a Numpy array (for illustrative purposes).  The array will look 
something like:
            data = np.array([[[0.0,0.0,0.0],[0.2,0.5,0.7],[0.3,0.5,0.6],...]]])

where the inner array represents the RGB value (in the range 0.0 to 1.0) for an individual x-y pixel:
            [0.2, 0.6, 0.8]
and 0.0 is black and 1.0 is full colour.  Sometimes, we specify RGB as integers (in the range 0 to 255).  The
above RGB value would be (multiply each value by 255):
            [51, 153, 240]

In the example below, the array is 11x11x3.  Therefore the image is 11x11 with 3 colours.  The pixels are
specified as floats (even though they look like ints).  This is a tiny images and so we can see it more clearly
I'm going to duplicate the image twice to get a 44x44 image using:
            data = np.vstack((data, data))
            data = np.hstack((data, data))

and make sure the values are floats (not ints):  
            data = data.astype(np.float_)

Now we display the image with:
            plt.imshow(data, interpolation = "none")

and then fill any holes in the image with:
            filled = nd.binary_fill_holes(data).astype(int)

However, this algorithm only works with monochrome images.  Since the pixel values in the example are all
either
            [0, 0, 0] (black) or 
            [1, 1, 1] (white)

the image is in fact a black and white image.  We can just pick one of the color channels to convert the image 
to monochrome.  I've chosen red (channel 0):
            data = data[:,:,0]

Finally we get "skimage.measure" to count the number of objects in the image.  The way "skimage.measure" works 
is to label the adjacent non black images with integers starting with 1, up to the number of images found.  The 
start of the modified array looks like: 
            [[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
             [ 0  1  1  1  1  0  2  2  2  2  0  0  3  3  3  3  0  4  4  4  4  0]
             [ 0  1  1  1  1  0  2  2  2  2  0  0  3  3  3  3  0  4  4  4  4  0]
             [ 0  1  1  1  1  0  2  2  2  2  0  0  3  3  3  3  0  4  4  4  4  0]
             [ 0  1  1  0  0  0  2  2  2  2  0  0  3  3  0  0  0  4  4  4  4  0]
             [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]

showing the first 4 labels.  As the label number increases, the colormap changes the object's color.  The resulting
array can now be used to calculate not just the number of images, but also the area and centroid of each object.  
These are displayed in the final image.

Note: make sure you close each image to get to the next image as the program runs.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import skimage.measure as measure

def set_title(title):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title(title)

data = np.array(
        [ 
            [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[0,0,0],[1,1,1],[0,0,0],[0,0,0],[1,1,1],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[0,0,0],[0,0,0],[1,1,1],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
            [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[1,1,1],[0,0,0],[0,0,0],[1,1,1],[0,0,0],[1,1,1],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[0,0,0],[0,0,0],[1,1,1],[0,0,0],[1,1,1],[0,0,0]],
            [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
        ],
    )

# duplicate image
data = np.vstack((data, data))
data = np.hstack((data, data))
data = data.astype(np.float_)

set_title("black and white image")
plt.imshow(data, interpolation = "none")
plt.show()

set_title("convert to single channel and fill holes")
data = data[:,:,0]
filled = nd.binary_fill_holes(data).astype(int)
plt.imshow(filled, interpolation = "none", cmap = "jet")
plt.show()

labels = measure.label(filled)
print(labels)
props = measure.regionprops(labels)
set_title("label objects: {} objects found".format(len(props)))

# label all the items with number and size
for item in props:
    b = item['bbox']
    x = (b[0] + b[2])/2
    y = (b[1] + b[3])/2
    n = item['Label']
    message = str(item['Label']) + " : " + str(item['FilledArea'])
    plt.text(x, y, message, color="white")

plt.imshow(labels, interpolation = "none", cmap = "jet")
plt.show()
