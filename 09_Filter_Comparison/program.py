"""
Program 9: Mean vs Gaussian vs Median
Adds salt-and-pepper noise to the base input image (overwriting
input.jpg so it visibly contains noise), then applies Mean, Gaussian
and Median filters to that same noisy image and saves all three
results separately.
"""

import cv2
import numpy as np

def add_salt_and_pepper_noise(image, amount=0.04):
    noisy = image.copy()
    h, w = image.shape[:2]
    num_pixels = int(amount * h * w)

    ys = np.random.randint(0, h, num_pixels // 2)
    xs = np.random.randint(0, w, num_pixels // 2)
    noisy[ys, xs] = 255  # salt

    ys = np.random.randint(0, h, num_pixels // 2)
    xs = np.random.randint(0, w, num_pixels // 2)
    noisy[ys, xs] = 0  # pepper

    return noisy

# Read base image and create a noisy version
base_img = cv2.imread("input.jpg")
noisy_img = add_salt_and_pepper_noise(base_img, amount=0.04)

# Overwrite input.jpg with the noisy version (same noisy input for all filters)
cv2.imwrite("input.jpg", noisy_img)
noisy_img = cv2.imread("input.jpg")

# Apply Mean filter
mean_filtered = cv2.blur(noisy_img, (5, 5))
cv2.imwrite("output_mean.png", mean_filtered)

# Apply Gaussian filter
gaussian_filtered = cv2.GaussianBlur(noisy_img, (5, 5), 0)
cv2.imwrite("output_gaussian.png", gaussian_filtered)

# Apply Median filter
median_filtered = cv2.medianBlur(noisy_img, 5)
cv2.imwrite("output_median.png", median_filtered)

print("Mean, Gaussian and Median filters applied to the same noisy input.")
