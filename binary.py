#binary image==== black & white image
#black = 0px
#white = 1px

import cv2
 
img = cv2.imread('C:/Users/compaq-pc/Desktop/OpenCV tutorial/images/abc.jpg',0)
cv2.imshow("GrayImage", img)

cv2.waitKey(0)

#thresholding
ret, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("B&W", bw)
cv2.waitKey(0)

cv2.destroyAllWindows()
