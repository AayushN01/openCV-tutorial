#FInd out the shape of objects

import cv2
import numpy as np

img = cv2.imread("lenna.png", 0) #Gray conversion

height, width = img.shape

#Extract slop edges

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
                    #('original image(gray as argument),(datatype-64bit),width pixel, height pixel, kernel size')
cv2.imshow("Original Image", img)
cv2.waitKey(0)

cv2.imshow('Sobel X image', sobel_x)
cv2.waitKey(0)

cv2.imshow('Sobel Y image', sobel_y)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Sobel OR", sobel_or)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian Image', laplacian)
cv2.waitKey(0)

canny = cv2.Canny(img, 20, 170) #uses gradient values as threshold
cv2.imshow('Canny Edge', canny)
cv2.waitKey(0)


