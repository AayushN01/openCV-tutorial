import cv2

img = cv2.imread('icon.png')

cv2.imshow('Output Image', img)

cv2.waitKey() #wait till key interrupt is received

cv2.destroyAllWindows()
