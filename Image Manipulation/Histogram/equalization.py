# Only for GrayScale
from matplotlib import pyplot as plt
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#BGR TO GRAY
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Grey", grey)
cv2.waitKey(0)

eq = cv2.equalizeHist(grey)
cv2.imshow("NORAML AND EQUALIZED", np.hstack([grey, eq]))
cv2.waitKey(0)