import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
time.sleep(2)
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, im = cap.read()
    ret, frame= cap.read()
    im = cv2.resize(im,(509,284))
    frame = cv2.resize(frame,(509,284))
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    temp = cv2.imread("qrt.png",0)

    w, h = temp.shape[::-1]

    res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res>=threshold)
    i=0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
        print "Detected"
        i=i+1
        if i ==5 or i==10 :
            cv2.imwrite(str(i)+"s.png",im)
            continue
    cv2.imshow('detected',im)
    cv2.imshow('cam',frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()