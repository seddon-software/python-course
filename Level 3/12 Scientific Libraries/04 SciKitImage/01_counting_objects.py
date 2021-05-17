import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import skimage.measure as measure

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

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
