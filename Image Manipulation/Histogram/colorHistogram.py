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

# Split Channel
chans = cv2.split(image)

#Initialize a tuple
colors = ("b", "g", "r")

#Plot
plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
 
for (chan, color) in zip(chans, colors):

    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])


plt.show()
cv2.waitKey(0) 