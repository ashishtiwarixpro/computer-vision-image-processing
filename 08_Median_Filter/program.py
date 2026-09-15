import cv2
import numpy as np

def add_noise(image, amount=0.04):

    noisy = image.copy()

    height, width = image.shape[:2]

    total_pixels = int(amount * height * width)

    y = np.random.randint(0, height, total_pixels // 2)
    x = np.random.randint(0, width, total_pixels // 2)

    noisy[y, x] = 255

    y = np.random.randint(0, height, total_pixels // 2)
    x = np.random.randint(0, width, total_pixels // 2)

    noisy[y, x] = 0

    return noisy


img = cv2.imread("input.jpg")

noisy = add_noise(img)

cv2.imwrite("input.jpg", noisy)

noisy = cv2.imread("input.jpg")

result = cv2.medianBlur(noisy, 5)

cv2.imwrite("output.png", result)

print("Salt and pepper noise added")
print("Median filter applied")