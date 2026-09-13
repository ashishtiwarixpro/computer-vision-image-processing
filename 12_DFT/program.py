"""
Program 12: 2D DFT Computation
Reads a grayscale image, computes its 2D DFT using OpenCV, and
shifts the frequency representation so the low-frequency region
is centered. Prints the shapes of each stage. Also saves a viewable
magnitude output as required.
"""

import cv2
import numpy as np

# Read image and convert to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to the numeric type required by cv2.dft (float32)
gray_float = np.float32(gray)

# Compute the 2D DFT (2 channels: real and imaginary)
dft = cv2.dft(gray_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift the zero-frequency (low frequency) component to the center
dft_shifted = np.fft.fftshift(dft)

print("Original image shape:", gray.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT result shape:", dft_shifted.shape)

# Produce a viewable magnitude image as the saved output
magnitude = cv2.magnitude(dft_shifted[:, :, 0], dft_shifted[:, :, 1])
magnitude_log = 20 * np.log(magnitude + 1)
magnitude_norm = cv2.normalize(magnitude_log, None, 0, 255, cv2.NORM_MINMAX)
magnitude_norm = np.uint8(magnitude_norm)

cv2.imwrite("output.png", magnitude_norm)
