#resizing technique
# can perform without knowing dmension 

import cv2
import numpy as pd

img = cv2.imread('lenna.png')
smaller = cv2.pyrDown(img) #reduce size pyrDown
larger = cv2.pyrUp(img) #enlarge image pyrU

cv2.imshow('Original', img)
cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)

cv2.waitKey(0)
cv2.destroyAllwindows()
