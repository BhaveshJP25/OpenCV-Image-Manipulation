import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help ="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#Translation
shifted = imutils.translate(image, 100, 100)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
#Rotate
rotated = imutils.rotate(image, 45, scale = 0.5)
cv2.imshow("Rotate by 180", rotated)
cv2.waitKey(0)
#Resize
resize = imutils.resize(image, width = 100)
cv2.imshow("Resize", resize)
cv2.waitKey(0)
#flip
flipped = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", flipped)
flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("Both Flip", flipped)
cv2.waitKey(0)
#cropping
cropped = image[15:222, 150:400]
cv2.imshow("Crop", cropped)
cv2.waitKey(0)