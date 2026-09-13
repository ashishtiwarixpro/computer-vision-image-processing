"""
Program 11: Smoothing and Sharpening Comparison
Using the same input image, generates one smoothed output and one
sharpened output, saving them separately.
"""

import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

# --- Smoothing (Gaussian blur) ---
smoothed = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imwrite("output_smooth.png", smoothed)

# --- Sharpening (custom kernel via filter2D) ---
sharpening_kernel = np.array([
    [ 0, -1,  0],
    [-1,  9, -1],
    [ 0, -1,  0]
])
sharpened = cv2.filter2D(img, -1, sharpening_kernel)
cv2.imwrite("output_sharp.png", sharpened)

print("Smoothed and sharpened outputs generated from the same input image.")
