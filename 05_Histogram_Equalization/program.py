"""
Program 5: Histogram Equalization with Before/After Comparison
Performs histogram equalization on a grayscale image, saves the
equalized image, and saves a single plot comparing the histogram
before and after equalization.
"""

import cv2
import matplotlib.pyplot as plt

# Read image and convert to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
equalized = cv2.equalizeHist(gray)

# Save the equalized image (required output)
cv2.imwrite("output.png", equalized)

# Calculate histograms before and after equalization
hist_before = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()
hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256]).flatten()

# Plot both histograms in a single comparison figure
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(hist_before, color="blue")
plt.title("Histogram Before Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.plot(hist_after, color="green")
plt.title("Histogram After Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()

# Save the comparison plot (required output)
plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()
