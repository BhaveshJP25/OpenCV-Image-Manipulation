# Histogram  NUmber Of Pixels X Intensity
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

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)