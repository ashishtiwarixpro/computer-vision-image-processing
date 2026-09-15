import cv2

img = cv2.imread("input.jpg")

small = cv2.blur(img, (3, 3))

print("3x3 mean filter applied")

large = cv2.blur(img, (9, 9))

print("9x9 mean filter applied")

cv2.imwrite("output.png", large)

print("Output saved successfully")