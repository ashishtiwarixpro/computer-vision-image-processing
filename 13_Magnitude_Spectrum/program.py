"""
Program 13: Magnitude Spectrum
Computes the DFT and centered magnitude spectrum of a grayscale
image, applying log scaling for visualization, and saves it.
"""

import cv2
import numpy as np

# Read image and convert to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the DFT
gray_float = np.float32(gray)
dft = cv2.dft(gray_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Center the low frequencies
dft_shifted = np.fft.fftshift(dft)

# Compute magnitude from the real and imaginary parts
magnitude = cv2.magnitude(dft_shifted[:, :, 0], dft_shifted[:, :, 1])

# Apply log scaling so the wide dynamic range becomes visible
magnitude_spectrum = 20 * np.log(magnitude + 1)

# Normalize to 0-255 for saving as an image
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
magnitude_spectrum = np.uint8(magnitude_spectrum)

# Save the magnitude spectrum
cv2.imwrite("output.png", magnitude_spectrum)

print("Magnitude spectrum computed and saved.")
