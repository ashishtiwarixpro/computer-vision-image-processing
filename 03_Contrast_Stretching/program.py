import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_value = np.min(gray)
max_value = np.max(gray)

print("Minimum value:", min_value)
print("Maximum value:", max_value)

stretched = (gray.astype(np.float32) - min_value) * 255 / (max_value - min_value)

stretched = np.clip(stretched, 0, 255)
stretched = stretched.astype(np.uint8)

cv2.imwrite("output.png", stretched)

print("New minimum:", np.min(stretched))
print("New maximum:", np.max(stretched))