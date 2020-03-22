import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("Original image", img)
cv2.waitKey(0)

blur = cv2.blur(img,(3,3)) #uses 3x3 kernel
cv2.imshow('Blur Image', blur)
cv2.waitKey(0)

#instead of box filter you can use Gaussian kernel
Gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gaussian blur", Gaussian)
cv2.waitKey(0) 

#Take median of all pixels under kernel area and central element is replaced with this median value
median = cv2.medianBlur(img,5)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)

#Bilatera filte is very effective in noise removal
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral blur Image", bilateral)
cv2.waitKey(0)

cv2.destroyALlWindows()