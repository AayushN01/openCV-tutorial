import cv2

img = cv2.imread("icon.png")

cv2.imshow("Original image",img)


cv2.waitKey(0)

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Scale IMage", grey_img)
cv2.waitKey(0)

cv2.destroyAllWindows()


# ##ALTERNATE METHOD
# img = cv2.imread("icon.png", 0)
# cv2.imshow("gray", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()