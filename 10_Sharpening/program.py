"""
Program 10: Image Sharpening Using a Custom Kernel
Creates a sharpening kernel and applies it using cv2.filter2D().
"""

import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

# Custom sharpening kernel:
# Center weight (9) boosts the current pixel while the surrounding
# -1's subtract neighboring pixel values, emphasizing edges/details.
# The weights sum to 1 so overall image brightness is preserved.
sharpening_kernel = np.array([
    [ 0, -1,  0],
    [-1,  9, -1],
    [ 0, -1,  0]
])

# Apply the kernel using filter2D
sharpened = cv2.filter2D(img, -1, sharpening_kernel)

# Save the sharpened result
cv2.imwrite("output.png", sharpened)

print("Sharpening kernel used:\n", sharpening_kernel)
