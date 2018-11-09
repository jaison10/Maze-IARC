from __future__ import print_function

import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

       
  

im = cv2.imread("mqr2.png")

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
         
decodedObjects = pyzbar.decode(im)
# Print results
for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')  
