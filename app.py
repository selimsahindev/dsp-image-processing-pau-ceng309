import cv2
import numpy as np
from matplotlib import pyplot as plt

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
contrast_stretching = cv2.LUT(img, table)

# Apply the GaussianBlur filter
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Show the images
cv2.imshow("Original Image", original)
cv2.imshow("Contrast Stretching", contrast_stretching)
cv2.imshow("Gaussian Blur", gaussian_blur)

# Draw all in one window and label them
cv2.imshow("All", np.hstack([original, contrast_stretching, gaussian_blur]))

# Save all of them in a folder named 'outputs'
cv2.imwrite("outputs/contrast_stretching.jpg", contrast_stretching)
cv2.imwrite("outputs/gaussian_blur.jpg", gaussian_blur)
cv2.imwrite("outputs/all.jpg", np.hstack([original, contrast_stretching, gaussian_blur]))

# Wait for any key to be pressed before closing the image
cv2.waitKey(0)
cv2.destroyAllWindows()
