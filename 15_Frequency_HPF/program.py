"""
Program 15: Frequency-Domain High-Pass Filtering
Creates and applies a high-pass mask that suppresses the central
low-frequency region and preserves higher-frequency content, then
performs the inverse operations to reconstruct the filtered image.
"""

import cv2
import numpy as np

# Read image and convert to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape
crow, ccol = rows // 2, cols // 2

# Compute the DFT and shift low frequencies to the center
gray_float = np.float32(gray)
dft = cv2.dft(gray_float, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shifted = np.fft.fftshift(dft)

# Create a high-pass mask: start with all-ones (keep everything),
# then block out a central circular region (removes low frequencies,
# keeps high frequencies / edges and fine detail).
mask = np.ones((rows, cols, 2), np.uint8)
radius = 40
cv2.circle(mask, (ccol, crow), radius, (0, 0), -1)

# Apply the mask to the shifted DFT
filtered_dft = dft_shifted * mask

# Inverse shift and inverse DFT to reconstruct the spatial-domain image
inverse_shifted = np.fft.ifftshift(filtered_dft)
reconstructed = cv2.idft(inverse_shifted)
reconstructed = cv2.magnitude(reconstructed[:, :, 0], reconstructed[:, :, 1])

# Normalize for saving as a viewable image
reconstructed = cv2.normalize(reconstructed, None, 0, 255, cv2.NORM_MINMAX)
reconstructed = np.uint8(reconstructed)

# Save the reconstructed high-pass filtered output
cv2.imwrite("output.png", reconstructed)

print("High-pass filter applied with blocked radius:", radius)
