import cv2
import numpy as np
import random as rnd
from os import listdir
from os.path import isfile, join
from imutils.object_detection import non_max_suppression

from sieve import Sieve as filter

templateDir = "templates/"
templates = [f for f in listdir(templateDir) if isfile(join(templateDir, f))]
image = cv2.imread("feladat.jpg")
#image = filter.wash(image)
#image = filter.wash(filter.sieve(image))
thres = 0.5

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

boxes = []

for template in templates:
    print(templateDir + template)
    templateGray = cv2.resize(cv2.imread(templateDir + template, cv2.IMREAD_GRAYSCALE), dsize=(0, 0), fx=0.3, fy=0.3)
    (tH, tW) = templateGray.shape[:2]

    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (ys, xs) = np.where(thres < result)

    rects = []
    for (x, y) in zip(xs, ys):
        rects.append((x, y, x + tW, y + tH))

    filtered = non_max_suppression(np.array(rects))
    
    for x in filtered:
        boxes.append((x, template))

    color = (rnd.randint(0, 255), 0, rnd.randint(0, 255))

recognitions = non_max_suppression(np.array(boxes))

for (startX, startY, endX, endY) in recognitions:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

cv2.imshow("Recognition", cv2.resize(image, dsize=(0, 0), fx=0.8, fy=0.8))
cv2.waitKey(0)