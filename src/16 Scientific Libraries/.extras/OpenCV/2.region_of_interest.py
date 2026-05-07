# We will calculate the region of interest
# by slicing the pixels of the image
import cv2
# Reading the image using imread() function
image = cv2.imread('images/rice.jpg')
roi = image[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)

resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey()