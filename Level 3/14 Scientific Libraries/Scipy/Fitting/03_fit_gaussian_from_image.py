from PIL import Image
import numpy, pylab
import _03_fit_gaussian as fg



def cropImage():
    # open the test data image - it needs cropping
    img = Image.open('gaussian.tif')
    print(img.size)
    box = 800, 350, 1000, 500
    img = img.crop(box)
    img.show()
    return img

img = cropImage()

# read the cropped image directly into a numpy array 
imarray = numpy.array(img)
print("Numpy array shape:", imarray.shape)
print("Cropped image size", img.size)

# Create the gaussian data
data = imarray
pylab.matshow(data, cmap='gist_rainbow')
params = fg.fitgaussian(data)
fit = fg.gaussian(*params)
pylab.contour(fit(*pylab.indices(data.shape)), cmap='copper')
ax = pylab.gca()
(height, x, y, width_x, width_y) = params

legend = """
x : {:.1f}
y : {:.1f}
width_x : {:.1f}
width_y : {:.1f}""".format(x, y, width_x, width_y)
pylab.text(x = 0.95, 
           y = 0.05, 
           s = legend, 
           fontsize = 16, 
           horizontalalignment = 'right', 
           verticalalignment = 'bottom', 
           transform = ax.transAxes)

pylab.show()

