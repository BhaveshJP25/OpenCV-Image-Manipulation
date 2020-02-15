import numpy as np
import cv2

canvas = np.zeros((300,300,3), dtype = "uint8")
#line
red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red, 3)
#rectangle
green = (0, 255, 0)
cv2.rectangle(canvas, (10,10), (60,60), green, -1)
#circle
blue = (255, 0 , 0)
cv2.circle(canvas, (100, 100), 10, blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#concentric circles
canvas = np.zeros((300,300,3), dtype = "uint8")
white = (255, 255, 255)
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white, 10)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#random circle
canvas = np.zeros((300,300,3), dtype = "uint8")

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)