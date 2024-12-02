import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path_new = r"C:\Users\sruth\Desktop\rawCR_flash\05-07-2022_1-XRayTest.png"
image_new = cv2.imread(image_path_new, cv2.IMREAD_GRAYSCALE)

# 1. Normalization
image_norm_new = cv2.normalize(image_new, None, 0, 255, cv2.NORM_MINMAX)

# 2. Skew Correction
coords_new = np.column_stack(np.where(image_norm_new > 0))
angle_new = cv2.minAreaRect(coords_new)[-1]
if angle_new < -45:
    angle_new = -(90 + angle_new)
else:
    angle_new = -angle_new
(h_new, w_new) = image_norm_new.shape[:2]
center_new = (w_new // 2, h_new // 2)
M_new = cv2.getRotationMatrix2D(center_new, angle_new, 1.0)
image_skew_corrected_new = cv2.warpAffine(image_norm_new, M_new, (w_new, h_new), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# 3. Image Scaling
image_scaled_new = cv2.resize(image_skew_corrected_new, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# 4. Noise Removal
image_denoised_new = cv2.fastNlMeansDenoising(image_scaled_new, h=30)


_, image_binarized_new = cv2.threshold(image_denoised_new, 127, 255, cv2.THRESH_BINARY)

# 7. Canny Edge Detection
edges = cv2.Canny(image_binarized_new, 50, 150)

# 8. Contour Detection
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours for child hierarchy
for i, contour in enumerate(contours):
    if hierarchy[0][i][3] != -1:  # Check if it's a child contour
        cv2.drawContours(image_binarized_new, [contour], -1, (0, 0, 0), 1)

# Save the final processed image
processed_image_path_new = r"C:\Users\sruth\Desktop\xrayimagesop\new_image.png"

# Display the processed image
plt.figure(figsize=(10, 8))
plt.imshow(image_binarized_new, cmap='gray')
plt.title('Processed Image with Edge Detection for OCR')
plt.axis('off')
plt.show()

# Output the path to the processed image
processed_image_path_new
