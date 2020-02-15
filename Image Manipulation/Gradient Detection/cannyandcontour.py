import numpy as np
import argparse
import cv2
#canny
# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (11,11), 0)

cv2.imshow("Gaussian blurr", blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", edged)


#contour 
(_,cnts,_)=cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0,255,0), 2)
cv2.imshow("Countours", coins)
cv2.waitKey(0)