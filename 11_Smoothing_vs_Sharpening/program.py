import cv2
import numpy as np

img = cv2.imread("input.jpg")

smooth = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imwrite("output_smooth.png", smooth)

kernel = np.array([
    [0, -1, 0],
    [-1, 9, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output_sharp.png", sharp)

print("Smoothing completed")
print("Sharpening completed")