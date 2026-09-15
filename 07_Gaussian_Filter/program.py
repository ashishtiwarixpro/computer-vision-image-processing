import cv2

img = cv2.imread("input.jpg")

kernel = (7, 7)

result = cv2.GaussianBlur(img, kernel, 0)

cv2.imwrite("output.png", result)

print("Gaussian filter applied")
print("Kernel size:", kernel)