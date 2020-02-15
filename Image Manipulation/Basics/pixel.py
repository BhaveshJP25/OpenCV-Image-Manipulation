import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(b, g, r) = image[0,0]
print("{}, {}, {}".format(r,g,b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0,0]
print("{}, {}, {}".format(r,g,b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)

image[0: 100, 0: 100] = (0,255,0)
cv2.imshow("Corner", image)
cv2.waitKey(0)

cv2.imwrite("cat.jpeg", image)