# USAGE
# python find_screen.py --query queries/query_marowak.jpg

# import the necessary packages

import time
import numpy as np
import argparse
import cv2
cap = cv2.VideoCapture(0)
time.sleep(2)

# construct the argument parser and parse the arguments
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	# load the query image, compute the ratio of the old height
	# to the new height, clone it, and resize it
	#image = cv2.imread("2.jpg")
	frame = cv2.resize(frame,(509,284))
	image = cv2.resize(frame,(509,284))
	ratio = image.shape[0] / 300.0
	orig = image.copy()
	#image = cv2.resize(image, (300,300))

	# convert the image to grayscale, blur it, and find edges
	# in the image
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	edged = cv2.Canny(gray, 30, 200)

	# find contours in the edged image, keep only the largest
	# ones, and initialize our screen contour
	_,cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
	screenCnt = None
	i=0
	# loop over our contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		rect=cv2.minAreaRect(contours(c))

		# if our approximated contour has four points, then
		# we can assume that we have found our screen
		if len(approx) == 4:
		
			screenCnt = approx
			i=1
			print cv2.contourArea(c)
			break
	if i==0 :
		print "No screen"
	elif cv2.contourArea(c)<90000:
		
		print "Forward"
	else:
		# draw a rectangle around the screen
		print "stop"
		orig = image.copy()
		cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
		cv2.imshow("Game Boy Screen", image)

		# create a mask for the screen
		mask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.drawContours(mask, [screenCnt], -1, 255, -1)
		mask=cv2.bitwise_and(orig, orig, mask = mask)
		
		cv2.imshow("Masked", mask)
	cv2.imshow("cam",frame)
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()