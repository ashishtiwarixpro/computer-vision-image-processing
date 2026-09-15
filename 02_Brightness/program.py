import cv2
import numpy as np

img = cv2.imread("input.jpg")

brightness = 60

before = img[50, 50].copy()

bright_img = cv2.add(img, np.full(img.shape, brightness, dtype=np.uint8))

cv2.imwrite("output.png", bright_img)

after = bright_img[50, 50]

print("Pixel before:", before)
print("Pixel after:", after)
print("Brightness added:", brightness)