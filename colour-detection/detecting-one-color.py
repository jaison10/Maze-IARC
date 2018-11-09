import cv2
import numpy as np

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(0)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "C:/Users/JAISON/Desktop/IARC/Autonomous codes/1/test_image.png"

# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

hsv = cv2.cvtColor(camera_capture, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (0, 0, 0), (70, 255,255))

# mask=np.zeros(camera_capture.shape[:2],dtype="uint8")   # creates a canvas with height and width of the image. 
# (cx,cy)=(camera_capture.shape[1] // 2, camera_capture.shape[0] //2)    #finding the center. 
# cv2.rectangle(mask, (cx-75, cy-75),(cx+75, cy+75),255,-1)   #creating a mask. (B/W)
# cv2.imshow("MASK IS:",mask)
# cv2.waitKey(0)

masked= cv2.bitwise_and(camera_capture, camera_capture,mask=mask)
cv2.imshow("mask applied image ", masked)
cv2.waitKey(0)
# ## mask of black (0,0,0) ~ (0, 0,0)
# mask = cv2.inRange(hsv, (0, 0, 0), (0,0,0))

# ## slice the green
# imask = mask>0
# green = np.zeros_like(camera_capture, np.uint8)
# green[imask] = camera_capture[imask]

## save 
cv2.imwrite("black.png", masked)

del(camera)
cap.release()
cv2.destroyAllWindows()
