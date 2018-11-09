import cv2

a= cv2.imread("hull1.jpg")
b= cv2.imread("hull2.jpg")
c= cv2.imread("hull3.jpg")
d= cv2.imread("hull4.jpg")





r=cv2.flip(im,-1)
cv2.imshow("result",r)
cv2.waitKey(0)