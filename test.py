import cv2
import numpy as np

from sieve import Sieve as filter

image = cv2.imread("feladat.jpg")

s = filter.wash(image)

cv2.imshow("Output", cv2.resize(image, dsize=(0, 0), fx=0.8, fy=0.8))
cv2.waitKey(0)