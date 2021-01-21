import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# show whole image
img = mpimg.imread('macy_parade.jpg')
print(f"Image dimensions: {img.shape}")
plt.imshow(img)
plt.show()

# show sub-image
subImage = img[500:700, 1200:1700, :]
print(f"Image dimensions: {subImage.shape}")
plt.imshow(subImage)
plt.show()

# show single color with cmap switched to greyscale
subImage = img[500:700, 1200:1700, 1]
print(f"Image dimensions: {subImage.shape}")
plt.imshow(subImage, cmap='gray', vmin=0, vmax=255)
plt.show()

