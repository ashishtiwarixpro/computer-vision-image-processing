import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray)

cv2.imwrite("output.png", equalized)

hist_before = cv2.calcHist(
    [gray], [0], None, [256], [0, 256]
)

hist_after = cv2.calcHist(
    [equalized], [0], None, [256], [0, 256]
)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(hist_before)
plt.title("Before Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.plot(hist_after)
plt.title("After Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("histogram_comparison.png")

plt.close()