import cv2
import numpy as pd

img = cv2.imread('lenna.png')

height, width = img.shape[:2]

#starting pixel coordinates('top left of cropping rectangle')
start_row, start_col = int(height*.25), int(width*.25)
#ending the pixel coordinates(bottom right)
end_row, end_col = int(height*.75), int(width*.75)

#Use indexing to crop image
cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('Original', img)
cv2.waitKey(0)

cv2.imshow('Ceopped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()
