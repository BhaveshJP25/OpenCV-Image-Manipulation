import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("BGR", image)
cv2.waitKey(0)

#BGR TO GRAY
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", grey)
cv2.waitKey(0)
#BGR TO HSV
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)
#BGR TO GRAY
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)