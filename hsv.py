#colorspace(H= Hue,S=Saturation,V= Value)
#H:0-180, S:0-255, V:0-255
import cv2

img= cv2.imread('icon.png')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#convert RGB-HSV

cv2.imshow('HSV IMAGE', img_HSV)
cv2.imshow('Hue CHannel', img_HSV[:, :, 0])
cv2.imshow('Saturation', img_HSV[:, :, 1])
cv2.imshow('Value CHannel', img_HSV[:, :, 2])

cv2.waitKey(0)

cv2.destroyAllWindows()

