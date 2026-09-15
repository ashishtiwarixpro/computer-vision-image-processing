import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dft = cv2.dft(
    gray,
    flags=cv2.DFT_COMPLEX_OUTPUT
)

shifted = np.fft.fftshift(dft)

print("Original shape:", img.shape)
print("Gray image shape:", gray.shape)
print("DFT shape:", dft.shape)
print("Shifted DFT shape:", shifted.shape)

magnitude = cv2.magnitude(
    shifted[:, :, 0],
    shifted[:, :, 1]
)

magnitude = 20 * np.log(magnitude + 1)

magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

cv2.imwrite("output.png", magnitude)