#IMAGE TRANSPOSE
import cv2
import numpy as np

img = cv2.imread("lenna.png")

#Store height and width of image
height, width = img.shape[:2]
print(height)
print(width)

rotated_img = cv2.transpose(img)
cv2.imshow("Rotated Image", rotated_img)
cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()