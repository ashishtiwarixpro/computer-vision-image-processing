"""
Program 6: Mean Filtering
Applies a mean/average filter using two different kernel sizes and
saves the result obtained using the larger kernel as the final output.
"""

import cv2

# Read the input image
img = cv2.imread("input.jpg")

# --- Run 1: smaller kernel ---
kernel_small = (3, 3)
smoothed_small = cv2.blur(img, kernel_small)
print(f"Applied mean filter with kernel size {kernel_small}")

# --- Run 2: larger kernel ---
kernel_large = (9, 9)
smoothed_large = cv2.blur(img, kernel_large)
print(f"Applied mean filter with kernel size {kernel_large}")

# Save the final required output using the LARGER kernel result
cv2.imwrite("output.png", smoothed_large)
print("Final output saved using the larger kernel:", kernel_large)
