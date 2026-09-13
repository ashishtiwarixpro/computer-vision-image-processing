"""
Program 3: Contrast Stretching
Finds the min/max intensity of a grayscale image and linearly
stretches the intensity range to expand the useful contrast range.
(This is NOT histogram equalization - it is a simple linear stretch.)
"""

import cv2
import numpy as np

# Read image and convert to grayscale (low-contrast source)
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find current minimum and maximum intensity values
min_val = np.min(gray)
max_val = np.max(gray)
print("Minimum intensity:", min_val)
print("Maximum intensity:", max_val)

# Linear contrast stretching formula:
# new_pixel = (pixel - min) * (255 / (max - min))
stretched = (gray.astype(np.float32) - min_val) * (255.0 / (max_val - min_val))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

# Save the contrast-stretched result
cv2.imwrite("output.png", stretched)

print("New minimum intensity:", np.min(stretched))
print("New maximum intensity:", np.max(stretched))
