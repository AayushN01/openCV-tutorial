#Image ko each pixel sanga arithmetic operation garne
import cv2
import numpy as np

img = cv2.imread('lenna.png')

cv2.imshow('Original Image', img)
cv2.waitKey(0)

M = np.ones(img.shape, dtype="uint8") * 150 #call ones matrix imgshape function called, ie original img ko size ko ones matrix create huncha)

added = cv2.add(img, M)
cv2.imshow('Added', added)

subt = cv2.subtract(img, M)
cv2.imshow("Subtracted", subt)

mul = cv2.multiply(img, M)
cv2.imshow("Multiply", mul)

cv2.waitKey(0)
cv2.destroyAllWindows()

