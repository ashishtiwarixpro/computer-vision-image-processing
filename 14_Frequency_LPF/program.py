import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = gray.shape

crow = rows // 2
ccol = cols // 2

gray = np.float32(gray)

dft = cv2.dft(
    gray,
    flags=cv2.DFT_COMPLEX_OUTPUT
)

shifted = np.fft.fftshift(dft)

mask = np.zeros(
    (rows, cols, 2),
    np.uint8
)

radius = 40

cv2.circle(
    mask,
    (ccol, crow),
    radius,
    (1, 1),
    -1
)

filtered = shifted * mask

inverse = np.fft.ifftshift(filtered)

result = cv2.idft(inverse)

result = cv2.magnitude(
    result[:, :, 0],
    result[:, :, 1]
)

result = cv2.normalize(
    result,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

result = np.uint8(result)

cv2.imwrite("output.png", result)

print("Low pass filter applied")