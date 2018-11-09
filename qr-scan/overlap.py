import cv2
import numpy as np

a = cv2.imread("hull1.jpg")
a=cv2.resize(a,(530,320))
b= cv2.imread("hull2.jpg")
b=cv2.resize(b,(530,320))
c = cv2.imread("hull3.jpg")
c=cv2.resize(c,(530,320))
d = cv2.imread("hull4.jpg")
d=cv2.resize(d,(530,320))

a = cv2.bitwise_not(a)
b = cv2.bitwise_not(b)
c = cv2.bitwise_not(c)
d = cv2.bitwise_not(d)
r = cv2.bitwise_and(a,b)
r1 = cv2.bitwise_and(c,d)
r = cv2.bitwise_and(r,r1)
r = cv2.bitwise_not(r)
cv2.imshow("a",r)
cv2.imwrite("mqr2.png",r)
cv2.waitKey(0)
cv2.destroyAllWindows()