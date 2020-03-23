import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow('Original Iamge', img)
cv2.waitKey(0)

kernel_sharpening = np.array([[-1, -1, -1, -1, -1],
                                [-1,-1, -1, -1, -1],
                                [-1,-1, 25, -1, -1],
                                [-1,-1, -1, -1, -1],
                                [-1,-1, -1, -1, -1]])


sharpened = cv2.filter2D(img,-1,kernel_sharpening)

cv2.imshow('Imahe sharpening', sharpened)
cv2.waitKey()
cv2.destroyAllWindows()
