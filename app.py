import cv2
import numpy as np

# Read the puppy.jpeg image from the 'images' folder
img = cv2.imread('images/puppy.jpeg')

# Make a copy of the original image
original = img.copy()

# Define the variables for addWeighted function
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')

# Apply contrast stretching
img = cv2.LUT(img, table)

cv2.imshow("Original Image", original)
cv2.imshow("Output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Wait for any key to be pressed
cv2.waitKey()