'''
This example uses a real image; the image is monochrome rather than colour, which means the RGB values 
are the same for each pixel (0 to 255), with 0 as black through to 255 as white.

Note the function:
            def enhanceImage(image, threshold):
                image[ image[:,:] <= threshold ] = 0
                image[ image[:,:]  > threshold ] = 255

which uses indexing to convert greylevels less than or equal to a given threshold to black (=0) and
all other pixels to white (=255).
'''

import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import skimage.measure as measure
import skimage.morphology as morphology
import scipy.ndimage as nd

def load_image( infilename ) :
    img = Image.open( infilename )
    data = np.asarray( img, dtype="int32" )
    return data

def set_title(title):
    figure = plt.gcf()
#    figure.canvas.set_window_title(title)

def enhanceImage(image, threshold):
    image[ image[:,:] <= threshold ] = 0
    image[ image[:,:]  > threshold ] = 255
    
rice = load_image("images/rice.jpg")
print("Shape of raw image: {}".format(rice.shape))

# algorithms work with monochrome images
rice = rice[:,:,0]
print(rice)
print("Shape of red image: {}".format(rice.shape))
set_title("monchrome image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

enhanceImage(rice, 120)
set_title("enhanced image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# remove small objects (they must be labelled)
set_title("removed small objects")
labelled = measure.label(rice)
labelled = morphology.remove_small_objects(labelled)

# remove the labelling because leads to a misleading display
# use the enhanceImage function (all objects have value >= 1, non objects = 0)
rice = np.copy(labelled)
enhanceImage(rice, 1)
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

set_title("close objects and fill holes")
rice = nd.binary_fill_holes(rice).astype(int)
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# look at object properties
rice = measure.label(rice)
props = measure.regionprops(rice)
for item in props:
    y = item.centroid[0]
    x = item.centroid[1]
    message = str(item.label)
    plt.text(x, y, message, color="white")
set_title("labelling {} objects".format(len(props)))
plt.imshow(rice, interpolation = "none", cmap = "jet")
plt.show()

