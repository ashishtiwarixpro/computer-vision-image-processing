"""
Program 2: Controlled Brightness Enhancement
Increases the brightness of an image by a chosen constant while
correctly handling the valid pixel-intensity range (0-255).
"""

import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

# Constant brightness value to add
brightness_value = 60

# Compare one pixel before enhancement (row=50, col=50)
sample_pixel_before = img[50, 50].copy()

# cv2.add clips values at 255 automatically (saturation, no overflow wrap-around)
brightened = cv2.add(img, np.full(img.shape, brightness_value, dtype=np.uint8))

# Save the enhanced image
cv2.imwrite("output.png", brightened)

# Compare the same pixel after enhancement
sample_pixel_after = brightened[50, 50]

print("Pixel value at (50,50) BEFORE brightening:", sample_pixel_before)
print("Pixel value at (50,50) AFTER brightening: ", sample_pixel_after)
print("Brightness constant added:", brightness_value)
