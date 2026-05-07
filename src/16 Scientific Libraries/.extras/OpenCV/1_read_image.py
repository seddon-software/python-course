# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('images/rice.jpg')
print(f"image type: {type(image)}")

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))
