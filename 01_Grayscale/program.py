import cv2

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output.png", gray)

height, width = gray.shape

print("Original image shape:", img.shape)
print("Grayscale image shape:", gray.shape)
print("Height:", height)
print("Width:", width)