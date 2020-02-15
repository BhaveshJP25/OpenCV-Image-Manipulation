import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#Addition
print("max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
#sub
print("wrap of max by np: {}".format(np.uint8([200])+np.uint8([100])))
print("wrap of min by np: {}".format(np.uint8([50])-np.uint8([100])))

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added image", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted image", subtracted)

cv2.waitKey(0)







