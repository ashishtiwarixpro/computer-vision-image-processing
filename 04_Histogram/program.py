import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

hist = hist.flatten()

peak = int(np.argmax(hist))
count = int(hist[peak])

print("Highest intensity:", peak)
print("Pixel count:", count)

plt.figure(figsize=(8, 5))

plt.plot(hist)

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.axvline(peak, linestyle="--")

plt.legend([f"Peak = {peak}"])

plt.tight_layout()

plt.savefig("output.png")

plt.close()