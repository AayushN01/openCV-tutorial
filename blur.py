import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow('Original image', img)
cv2.waitKey(0)

#Creating 3x3 Kernel(Kernel bata afno image pass garne ani o/p check garne ki kati blurring cha)
kernel_3x3 = np.ones((3,3), np.float32)/9 

#Using cv2.filter2D to convolve the kernel with image
blurred = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey(0)

#Cannot generate kernel in even number
kernel_7x7 = np.ones((7,7), np.float32)/49
blurred2 = cv2.filter2D(img, -1, kernel_7x7)
cv2.imshow("7x7 Kernel BLurring", blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()