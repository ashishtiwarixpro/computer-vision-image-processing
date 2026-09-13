"""
Program 4: Histogram Analysis
Calculates and plots the intensity histogram of a grayscale image
and prints the intensity value having the highest frequency.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image and convert to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram (256 bins for intensities 0-255)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()

# Find the intensity value with the highest frequency
peak_intensity = int(np.argmax(hist))
peak_count = int(hist[peak_intensity])

print("Intensity value with highest frequency:", peak_intensity)
print("Frequency (pixel count) at that intensity:", peak_count)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.plot(hist, color="black")
plt.title("Grayscale Intensity Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.axvline(peak_intensity, color="red", linestyle="--",
            label=f"Peak = {peak_intensity}")
plt.legend()
plt.tight_layout()

# Save the histogram plot (required output)
plt.savefig("output.png", bbox_inches="tight")
plt.close()
