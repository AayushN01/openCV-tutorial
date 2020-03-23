import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read() #ret ko through camera ko string read garcha ani access throug frame
    cv2.imshow('Our Live Sketch', frame)

    if cv2.waitKey(1)==13: #13 being ASCII of ENTER
        break
cap.release()
cv2.destroyALlWindows()
