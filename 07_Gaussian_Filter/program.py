"""
Program 7: Gaussian Smoothing
Applies Gaussian smoothing to an image and saves the result.
"""

import cv2

# Read the input image
img = cv2.imread("input.jpg")

# Kernel size 7x7 chosen: it is odd (required by Gaussian blur),
# and large enough to visibly reduce noise while still keeping
# the main facial/edge structure recognizable (not overly blurred
# like a bigger kernel, e.g. 15x15, would cause).
kernel_size = (7, 7)
sigma = 0  # 0 lets OpenCV compute sigma automatically from kernel size

gaussian_smoothed = cv2.GaussianBlur(img, kernel_size, sigma)

# Save the smoothed result
cv2.imwrite("output.png", gaussian_smoothed)

print("Gaussian smoothing applied with kernel size:", kernel_size)
