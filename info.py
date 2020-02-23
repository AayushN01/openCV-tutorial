import cv2
#image pixel info

img = cv2.imread('icon.png')

cv2.imshow('Output', img)
print(img.shape)

print("Height pixel values:", img.shape[0])
print("Width pixel value", img.shape[1])


cv2.waitKey(0)
cv2.destroyAllWindows()